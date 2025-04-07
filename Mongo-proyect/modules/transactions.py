# Importaci'on de módulos necesarios
from rich.console import Console # Módulo para mejorar la presentación en consola
from rich.table import Table    # Módulo para crear tablas en consola 
from rich.panel import Panel    # Módulo para crear paneles decorativos
from pymongo import MongoClient # Módulo oficial de MongoDB para Python 
import random                   # Módulo para generar números aleatorios

# Creación de una instancia de Console para la interfaz 
console = Console()

def create_sample_transaction_data(db):
    """
    Crea datos de ejemplo para transacciones 
    
    Args:
        db: Instancia de base de datos MongoDB
    """
    # Crear cuentas bancarias de ejemplo 
    cuentas =  [
        {"cuenta_id": 1, "titular": "Juan Pérez", "balance": 1000.0},
        {"cuenta_id": 2, "titular": "María Gómez", "balance": 1500.0},
        {"cuenta_id": 3, "titular": "Empresa XYZ", "balance": 5000.0},
        {"cuenta_id": 4, "titular": "Carlos Ruiz", "balance": 750.0},
        {"cuenta_id": 5, "titular": "Ana López", "balance": 3000.0},
    ]
    
    # insert_many() - Método para insertar múltiples documentos
    db["cuentas"].insert_many(cuentas)
    
    # create_collection() - Método para crear una nueva colección
    db.create_collection("movimientos")
    
    console.print("✅ [green]Colecciones 'cuentas' y 'movimientos' creadas[/green]")
    
def run(db):
    """
    Módulo de Transacciones en MongoDB

    Args:
        db: Instancia de base de datos MongoDB
        
    Este módulo demuestra:
        - Operaciones sin transacciones
        - Transacciones ACID 
        - Manejo de errores y rollback
        - Seguimiento de movimientos
    """
    console-print(Panel.fit("🟦 [bold cyan]Transacciones en MongoDB[/bold cyan]🟦"))
    
    # Verificar y crear colecciones de ejemplosi no existen 
    if "cuentas" not in db.list_collection_names():
        console.print("\n🔄️ Creando colecciones 'cuentas' y 'movimientos'...")
        create_sample_transaction_data(db)
        
    while True:
        # Crear tabla de menú con opciones disponibles
        table = Table(title="Operciones Transaccionales", show_header=True)
        table.add_column("Opción", style="cyan")
        table.add_column("Operción", style="green")
        table.add_column("Descripción", style="white")
        
        # Agregar opciones al menú 
        table.add_row("1", "Transferencia simple", "Mover dinero entre cuenta (sin transacción)")
        table.add_row("2", "Transferencia transaccional", "Mover dinero con transacción ACID")
        table.add_row("3", "Transaccion fallida", "Transacción fallida", "Simular error y rollback")
        table.add_row("4", "Ver estado cuentas", "Mostrar saldos actuales")
        table.add_row("0", "Volver", "Regresar al menú principal")
        
        console.print(table)
        
        choice = console.input("\n 🔹Seleccione una operación (0-4): ")
        
        if choice == "0":
            break
        
        elif choice == "1":
            # Transferencia sin transacción (operaciones individuales)
            console.print("\n[bold]Transferencia SIN Transacción:[/bold]")
            from_acc = console,input("Cuenta origen (1-5): ")
            to_acc = console.input("Cuenta destino (1-5): ")
            amount = float(console.input("Monto a tranferir: "))
            
            try: 
                # update_one() - Método para actualizar un documento
                # $inc - Operador para incremento/decremento
                db["cuentas"].update_one(
                    {"cuenta_id": int(from_acc)},
                    {"$inc": {"balance": -amount}}
                )
                db["cuentas"].update_one(
                    {"cuenta_id": int(to_acc)},
                    {"$inc": {"balance": amount}}
                )
                
                # inseet_one() - Método para insertar un documento
                db["movimientos"].insert_one({
                    "tipo": "transferencia",
                    "origen": int(from_acc),
                    "destino": int(to_acc),
                    "monto": amount,
                    "estado": "completado"
                })
                
                console.print("\n✅ [green]Transferencia completada (sin transacción)[/green]")
            except Exception as e:
                console.print(f"\n❌ [red]Eror: {e}[/red]")
                
        elif choice == "2":
            # Transferencia con transacción ACID 
            console.print("\n[bold]Transferencia Con Transacción:[/bold]")
            from_acc = console.input("Cuenta origen (1-5): ")
            to_acc = console.input("Cuenta destino (1-5): ")
            amount = float(console.input("Monto a transferir: "))
                
            # start_session() - Método para iniciar una sesión de transacción 
            session = db.client.start_session()
            try:
                # start_transaction() - Método para iniciar una transacción
                with session.start_transaction():
                    # Verificar fondos suficientes
                    cuenta_origen = db["cuentas"].find_one(
                        {"cuenta_id": int(from_acc)},
                        session=session
                    )
                    if cuenta_origen["balance"] < amount:
                        raise ValueError("Fondos insuficientes")
                    
                    # Actualizar ambas cuentas dentro de la transacción
                    db["cuentas"].update_one(
                        {"cuenta_id": int(from_acc)},
                        {"$inc": {"balance": -amount}},
                        session=session
                    )
                    db["cuentas"].update_one(
                        {"cuenta_id": int(to_acc)},
                        {"$inc": {"balance": amount}},
                        session=session
                    )
                    
                    # Registrar el movimiento dentro de la transacción
                    db["movimientos"].insert_one({
                        "tipo": "transferencia",
                        "origen": int(from_acc),
                        "destino": int(to_acc),
                        "monto": amount,
                        "estado": "completo"
                    }, sesion=session)
                    
                    # commit_transaction() - Método para confirmar la transacción
                    session.commit_transaction()
                    console.print("\n✅ [green]Transacción completada con éxito[\green]")
                    
            except Exception as e:
                # abort_transaction() - Método para cancelar la transacción
                session.abort_transaction()
                console.print(f"\n❌ [red]Transacción fallida (rollback): {e}[/red]")
            finally:
                # end_session() - Método para finalizar la sesión
                session.end_session()
                
        elif choice == "3":
            # Simulación de transacción fallida
            console.print("\n[bold]Simular Transacción Fallida:[/bold]")
            console.print("Se transferirá $100 pero se forzará un error")
            
            session = db.client.start_session()
            try:
                with session.start_transaction():
                    # Realizar operaciones válidas
                    db["cuentas"].update_one(
                        {"cuenta_id": 1},
                        {"$inc": {"balance": -100}},
                        session=session
                    )
                    db["cuentas"].update_one(
                        {"cuenta_id": 2},
                        {"$inc": {"balance": 100}},
                        session=session
                    )
                    
                    #Forzar un error para demostrar el rollback
                    raise ValueError("Error simulado en la transacción")
                
                    # Este código nunca se ejecutará
                    session.commit_transaction()
                    
            except Exception as e:
                session.abort_transaction()
                console.print(f"\n❌ [red]Transacción fallida (esperando): {e}[/red]")
                console.print("✅ [green]Se realizó rollback automático[/green]")
            finally: 
                session.end_session()
                
        elif choice == "4":
            # Mostrar estado actual de las cuentas
            console.print("\n[bold]Estado Actual de Cuentas:[/bold]")
            # find() - Método para buscar documentos
            # sort() - Método para ordenar resultados
            cuentas = list(db["cuentas"].find().sort("cuenta_id", 1))
            
            table = Table(title="Saldos de Cuentas", show_header=True)
            table.add_column("Cuenta ID")
            table.add_column("Titular")
            table.add_column("Balance")
            
            for cuenta in cuentas:
                table.add_row(
                    str(cuenta["cuenta_id"]),
                    cuenta["titular"],
                    f"${cuenta['balance']:.2f}"
                )
                
            console.print(table)
            
            # Mostrar últimos movimientos
            # limit() - Método para limiar resultados
            movimientos = list(db["movimientos"].find().sort("_id", -1).limit(5))
            if movimientos: 
                console.print("\n[bold]Últimos 5 movimientos:[/bold]")
                mov_table = Table(sow_header=True)
                mov_table.add_column("Fecha")
                mov_table.add_column("Tipo")
                mov_table.add_column("Detalle")
                mov_table.add_column("Monto")
                
                for mov in movimientos: 
                    detalle = f"{mov.get('origen', "")} → {mov.get('destino', "")}"
                    mov_table.add_row(
                        str(mov["_id"].generation_time),
                        mov["tipo"],
                        detalle, 
                        f"${mov['monto']:.2f}"
                    )
                    
                console.print(mov_table)
                
        else:
            console.print("\n❌ [red]Opción inválida. Intente nuevamente.[/red]")
        
        console.input("\nPresione Enter para continuar...")
        console.clear()