from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from bson.json_util import dumps
import json
import random
from datetime import datetime

console = Console()

def run(db):
    console.print(Panel.fit("  [bold cyan]Agregaciones en MongoDB[/bold cyan] "))

    if "ventas" not in db.list_collection_names():
        console.print("\n  Creando colección 'ventas' con datos de ejemplo...")
        create_sample_sales_data(db)

    collection = db["ventas"]

    while True:
        table = Table(title="Operaciones de Agregación", show_header=True)
        table.add_column("Opción", style="cyan")
        table.add_column("Operación", style="green")
        table.add_column("Descripción", style="white")

        table.add_row("1", "Agregación básica", "Ejemplo: Conteo y suma de ventas")
        table.add_row("2", "Agregación por campos", "Agregar por categoría/producto")
        table.add_row("3", "Filtros en pipelines", "Filtrar antes de agrupar")
        table.add_row("4", "Operadores avanzados", "Uso de $lookup, $unwind")
        table.add_row("5", "Pipeline personalizado", "Escribir tu propio pipeline")
        table.add_row("6", "Análisis temporal", "Agregaciones por fecha")
        table.add_row("7", "Estadísticas avanzadas", "Métricas y análisis detallado")
        table.add_row("0", "Volver", "Regresar al menú principal")

        console.print(table)

        choice = console.input("\n+ Seleccione una operación (0-7): ")

        if choice == "0":
            break
        
        elif choice == "1":
            console.print("\n[bold]Agregación Básica:[/bold] Conteo y total de ventas")
            pipeline = [
                {
                    "$group": {
                        "_id": None,
                        "total_ventas": {"$sum": "$monto"},
                        "cantidad_ventas": {"$sum": 1},
                        "promedio_ventas": {"$avg": "$monto"},
                        "venta_minima": {"$min": "$monto"},
                        "venta_maxima": {"$max": "$monto"}
                    }
                }
            ]
            print_aggregation(collection, pipeline)

        elif choice == "2":
            console.print("\n[bold]Agrupación por Producto:[/bold] Análisis detallado de datos") 
            pipeline = [
                {
                    "$group": {
                        "_id": "$producto",
                        "total_ventas": {"$sum": "$monto"},
                        "cantidad_ventas": {"$sum": 1},
                        "promedio_ventas": {"$avg": "$monto"},
                        "venta_minima": {"$min": "$monto"},
                        "venta_maxima": {"$max": "$monto"}
                    }
                },
                {
                    "$project": {
                        "producto": "$_id",
                        "total_ventas": {"$round": ["$total_ventas", 2]},
                        "cantidad_ventas": 1,
                        "promedio_ventas": {"$round": ["$promedio_ventas", 2]},
                        "venta_minima": {"$round": ["$venta_minima", 2]},
                        "venta_maxima": {"$round": ["$venta_maxima", 2]}
                    }
                },
                {"$sort": {"total_ventas": -1}}
            ]        
            print_aggregation(collection, pipeline)

        elif choice == "3":
            console.print("\n[bold]Filtros en Pipeline:[/bold] Análisis de ventas filtradas")
            min_amount = float(console.input("Monto mínimo a filtrar: ") or "100")

            pipeline = [
                {
                    "$match": {
                        "monto": {"$gte": min_amount}
                    }
                },
                {
                    "$group": {
                        "_id": "$producto",
                        "total_ventas": {"$sum": "$monto"},
                        "cantidad_ventas": {"$sum": 1},
                        "promedio_ventas": {"$avg": "$monto"},
                    }
                },
                {
                    "$project": {
                        "producto": "$_id",
                        "total_ventas": {"$round": ["$total_ventas", 2]},
                        "cantidad_ventas": 1,
                        "promedio_ventas": {"$round": ["$promedio_ventas", 2]},
                    }    
                },
                {"$sort": {"total_ventas": -1}}
            ]
            print_aggregation(collection, pipeline)

        elif choice == "4":
            console.print("\n[bold]Operaciones Avanzadas:[/bold] Join con productos")

            if "productos" not in db.list_collection_names():
                productos = [
                    {"nombre": "Laptop", "categoria": "Tecnología", "proveedor": "Techcorp"},
                    {"nombre": "Smartphone", "categoria": "Tecnología", "proveedor": "MobileTech"},
                    {"nombre": "Camisa", "categoria": "Ropa", "proveedor": "FashionStyle"},
                    {"nombre": "Zapatos", "categoria": "Calzado", "proveedor": "FootWear"},
                    {"nombre": "Libro", "categoria": "Librería", "proveedor": "BookStore"}
                ]
                db["productos"].insert_many(productos)
                console.print("  [green]Colección 'productos' creada[/green]")

            pipeline = [      
                {
                    "$lookup": {
                        "from": "productos",
                        "localField": "producto",
                        "foreignField": "nombre",
                        "as": "info_producto",
                    }   
                },
                {"$unwind": "$info_producto"},
                {
                    "$group": {
                        "_id": {
                            "categoria": "$info_producto.categoria",
                            "proveedor": "$info_producto.proveedor"
                        },
                        "total_ventas": {"$sum": "$monto"},
                        "cantidad_ventas": {"$sum": 1}
                    }
                },
                {
                    "$project": {
                        "categoria": "$_id.categoria",
                        "proveedor": "$_id.proveedor",
                        "total_ventas": {"$round": ["$total_ventas", 2]},
                        "cantidad_ventas": 1,
                    }   
                },
                {"$sort": {"total_ventas": -1}}
            ]
            print_aggregation(collection, pipeline)

        elif choice == "5":
            console.print("\n[bold]Pipeline Personalizado:[/bold]")
            console.print("""
            Ejemplo de pipeline:
            [
                {"$match": {"producto": "Laptop"}},
                {"$group": {
                    "_id": null,
                    "total": {"$sum": "$monto"},
                    "cantidad": {"$sum": 1}
                }}
            ]
            """)
            try:
                pipeline_input = console.input("Ingrese el pipeline (formato JSON): ")
                pipeline = json.loads(pipeline_input)
                print_aggregation(collection, pipeline)
            except Exception as e:            
                console.print(f"\nX [red]Error en el pipeline: {e}[/red]")

        elif choice == "6":
            console.print("\n[bold]Análisis Temporal:[/bold] Ventas por periodo")
            pipeline = [
                {
                    "$group": {
                        "_id": {
                            "año_mes": {"$substr": ["$fecha", 0, 7]},
                            "producto": "$producto"
                        },
                        "total_ventas": {"$sum": "$monto"},
                        "cantidad_ventas": {"$sum": 1}
                    }
                },
                {
                    "$project": {
                        "periodo": "$_id.año_mes",
                        "producto": "$_id.producto",
                        "total_ventas": {"$round": ["$total_ventas", 2]},
                        "cantidad_ventas": 1,
                    }  
                },
                {"$sort": {"periodo": 1, "total_ventas": -1}}
            ]
            print_aggregation(collection, pipeline)
            
        elif choice == "7":
            console.print("\n[bold]Estadísticas Avanzadas:[/bold] Análisis detallado")
            pipeline = [
                {
                    "$facet": {
                        "por_producto": [
                            {"$group": {
                                "_id": "$producto",
                                "total": {"$sum": "$monto"},
                                "cantidad": {"$sum": 1}
                            }},  
                            {"$sort": {"total": -1}}                            
                        ],
                        "por_metodo_pago": [
                            {"$group": {
                                "_id": "$metodo_pago",
                                "total": {"$sum": "$monto"},
                                "cantidad": {"$sum": 1}
                            }}
                        ],
                        "estadisticas_generales": [
                            {"$group": {
                                "_id": None,
                                "total_ventas": {"$sum": "$monto"},
                                "promedio_ventas": {"$avg": "$monto"},
                                "venta_maxima": {"$max": "$monto"},
                                "venta_minima": {"$min": "$monto"}
                            }}
                        ]
                    }
                }
            ]
            print_aggregation(collection, pipeline)
            
        else:
            console.print("\nX [red]Opción inválida. Intente nuevamente.[/red]")

        console.input("\nPresione Enter para continuar...")
        console.clear()
        
def print_aggregation(collection, pipeline):
    console.print("\n[bold]Pipeline ejecutado:[/bold]")
    console.print(dumps(pipeline, indent=2))
    
    try:
        results = list(collection.aggregate(pipeline))
        
        if not results:
            console.print("\n  No se encontraron resultados")
            return
        
        # Crear tabla dinámica basada en los resultados
        if isinstance(results[0], dict):
            table = Table(title="Resultados de agregación", show_header=True)
            
            # Manejar resultados de facet diferente
            if "por_producto" in results[0]:
                # Resultados de facet
                for facet_name in results[0].keys():
                    facet_data = results[0][facet_name]
                    if facet_data:
                        facet_table = Table(title=f"Faceta: {facet_name}", show_header=True)
                        for key in facet_data[0].keys():
                            if key != "_id":
                                facet_table.add_column(str(key))
                                
                        for doc in facet_data:
                            row_data = []
                            for key in doc.keys():
                                if key != "_id":
                                    value = doc[key]
                                    if isinstance(value, (int, float)):
                                        value = f"{value:,.2f}"
                                    row_data.append(str(value))
                            facet_table.add_row(*row_data)
                            
                        console.print(facet_table)
                        console.print(f"\nTotal en {facet_name}: {len(facet_data)}")
                return
            
            # Resultados normales
            for key in results[0].keys():
                if key != "_id":
                    table.add_column(str(key))
                    
            for doc in results:
                row_data = []
                for key in doc.keys():
                    if key != "_id":
                        value = doc[key]
                        if isinstance(value, (int, float)):
                            value = f"{value:,.2f}"
                        row_data.append(str(value))
                table.add_row(*row_data)
            
            console.print(table)
            
            if len(results) > 1:
                console.print(f"\nTotal de resultados: {len(results)}")
                
    except Exception as e:
        console.print(f"\nX [red]Error en agregación: {e}[/red]")
        
def create_sample_sales_data(db):
    productos = ["Laptop", "Smartphone", "Camisa", "Zapatos", "Libro"]  
    vendedores = [f"Vendedor-{i}" for i in range(1,6)]
    metodos_pago = ["tarjeta", "Efectivo", "Transferencia", "Crypto", "Paypal"]
    
    ventas = []
    
    for _ in range(1000):
        fecha = datetime(2023, random.randint(1, 12), random.randint(1, 28))    
        venta = {
            "producto": random.choice(productos),
            "monto": round(random.uniform(10, 1000), 2),
            "fecha": fecha.strftime("%Y-%m-%d"),
            "vendedor": random.choice(vendedores),
            "metodo_pago": random.choice(metodos_pago),
            "cantidad": random.randint(1, 5),
            "descuento": random.choice([0, 5, 10, 15, 20])
        }
        ventas.append(venta)
        
    db["ventas"].insert_many(ventas)
    console.print(f"\n  [green]Insertados {len(ventas)} ventas de ejemplo[/green]")