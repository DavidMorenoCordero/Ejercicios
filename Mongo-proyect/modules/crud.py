from rich.console import Console 
from rich.table import Table 
from rich.panel import Panel 
from bson.objectid import ObjectId 

console = Console()

def try_eval(value): 
    try: 
        return eval(value) 
    except: 
        return value 
def print_documents(docs): 

    if not docs: 
        console.print("No se encontraron documentos") 
        return 
    
    table = Table(title="Documentos Encontrados", show_header=True)
    for key in docs[0].keys():
        table.add_column(str(key))
    
    for doc in docs:
        row = []
        for val in doc.values():
            if isinstance(val, ObjectId):
                row.append(str(val))
        table.add_row(*row)
    console.print(table)

def run(db):
    console.print(Panel.fit("[bold cyan]operaciones CRUD en MongoDB[/bold cyan]"))

    collections = db.list_collection_names()
    if not collections:
        console.print("\n no hay colecciones en esta base de datos. creando una nueva...")
        collection_name = "ejemplo_crud"
        db.create_collection(collection_name)
    else:
        collection_name = console .input(f"\n ingrese el nombre de la coleccion({', '.join(collections)}):")
    collection = db[collection_name]

    while True:
        table = Table (title="operaciones crud", show_header=True)
        table.add_column("opcion", style="cyan")
        table.add_column("operacion", style="green")
        table.add_column("descripcion", style="white")

        table.add_row("1", "insertar", "agregar nuevos documentos")
        table.add_row("2", "buscar", "consultar documentos")
        table.add_row("3", "actualizar", "modificar documentos")
        table.add_row("4", "eliminar", "borrar documentos")
        table.add_row("5", "conteo", "contar documentos")
        table.add_row("0", "volver", "regresar al menu principal")

        console.print(table)

        choice = console.input("\n selecione una operacion CRUD (0.5): ")
        
        if choice == "0":

            break

        elif choice == "1":

            console.print("\n[bold]insertar documentos[/bold]") 
            console.print("1.insertar uno\n2. insertar varios datos")
            insert_choise = console.input("seleccione opcion (1-2): ")

            if insert_choise == "1":
                doc= {}
                while True:
                    key = console.input("ingrese clave (o deje vacio para terminar)")
                    if not key:
                        break
                    value = console,input(f"ingrese valor para '{key}': ")
                    doc[key] = try_eval(value)
                if doc:
                    result = collection.insert_one(doc)
                    console.print (f"\n [green]documento insertado con ID: {result.insert_id}[/green]") 
                else:
                    console.print (f"\n [red]no se proporcionaron datos para insertar [/red]")

            elif insert_choise == "2":
                docs =[]
                console.print("\nIngrese documentos (deje vacio para terminar): ")
                while True:
                    doc = {}
                    console.print(f"\ndocumento #{len(docs) +1}: ")
                    while True: 
                        key = console.input("ingrese clave (o deje vacio para terminar documento): ")
                        if not key:
                            break
                        value = console,input(f"ingrese valor para '{key}': ")
                        doc[key] = try_eval(value)
                    if doc:
                        docs.append(doc)
                    else: 
                        break
                if docs:
                    result = collection.insert_many(docs)
                    console.print (f"\n [green] insertados: {len(result.insert_ids)} documentos[/green]")
                    console.print (f"IDs: {result.inserted_ids}")
                else:
                    console.print (f"\n [red]no se proporcionaron documentos para insertar [/red]")
        elif choice == "2":
            console.print("\n[bold]Buscar documentos [/bold]")
            console.print("1. Buscar todos\n2. buscar con filtro\n3. buscar uno")
            find_choise = console.input("seleccione opcion (1-3): ")

            if find_choise == "1":
                docs = list(collection.find())
                print_documents(docs)

            elif find_choise == "2":
                try:
                    query = console.input("ingrese filtro (ej {'nombre': 'juan'}): ")
                    query = eval(query) if query else {}
                    docs = list(collection.find(query))
                    print_documents(docs) 
                except Exception as e: 
                    console.print(f"\n [red]Error en la consulta: {e}[/red]")
            

            elif find_choise == "3":
                try:
                    query = console.input("ingrese filtro (ej {'_id': ObjectId('...')}): ")
                    query = eval(query) if query else {}
                    doc = collection.find_one(query)
                    if doc:
                        print_documents([doc])
                    else:
                        console.print("\n no se encontraron documentos")
                except Exception as e: 
                    console.print(f"\n [red]Error en la consulta: {e}[/red]")

        elif choice == "3":
            console.print("\n[bold]Actualizar documentos[/bold]")
            console.print("1. actualizar uno\n2.actualizar varios")
            update_choise = console.input("selecione opcion(1-2):")

            if update_choise == "1":
                try:
                    filter_query = console.input("Ingrese filtro (ej: ('nombre': 'Juan'}): ")
                    update_query = console.input("Ingrese actualización (ej: {'$set': {'edad': 25}}): ")

                    filter_dict = eval(filter_query) if filter_query else {}
                    update_dict = eval(update_query) if update_query else {}

                    result = collection.update_one(filter_dict, update_dict)
                    console.print(f"\n [green] Documentos encontrados: {result.matched_count}[/green]")
                    console.print(f" [green] Documentos modificados: {result.modified_count}[/green]")

                except Exception as e:
                    console.print(f"\n[red] Error al actualizar: {e}[/red]")

            elif update_choise == "2":
                try:
                    filter_query = console.input("Ingrese filtro (ej: ('archivo': true}): ")
                    update_query = console.input("Ingrese actualización (ej: {'$set': {'estado': 'actualizado'}}): ")

                    filter_dict = eval(filter_query) if filter_query else {}
                    update_dict = eval(update_query) if update_query else {}

                    result = collection.update_many(filter_dict, update_dict)
                    console.print(f"\n [green] Documentos encontrados: {result.matched_count}[/green]")
                    console.print(f" [green] Documentos modificados: {result.modified_count}[/green]")

                except Exception as e:
                    console.print(f"\n[red] Error al actualizar: {e}[/red]")
                
        elif choice == "4":
            console.print("\n[bold]eliminar documentos[/bold]")
            console.print("1. eliminar uno\n2.eliminar varios")
            delete_choise = console.input("selecione opcion(1-2):")

            if delete_choise == "1":
                try:
                    query = console.input("ingrese filtro (ej {'_id': ObjectId('...')}): ")
                    query = eval(query) if query else {}
                    result = collection.delete_one(query)
                    console.print(f"\n [green] Documentos eliminados: {result.delete_count}[/green]")

                except Exception as e:
                    console.print(f"\n[red] Error al eliminar: {e}[/red]")

            elif choice == "2":
                try:
                    query = console.input("ingrese filtro (ej {'activo' : false}): ")
                    query = eval(query) if query else {}

                    count =  collection.count_documents(query)
                    if count > 0: 
                        confirm = console.input(f"se eliminaran {count} documentos. confirmar S/N: ")
                        if confirm.lower() == 'S':
                            result = collection.delete_many(query)
                            console.print(f"\n [green] documentos eliminados: {result.delete_count}[/green]")
                        else:
                            console.print(f"\n operacion cancelada")
                    else:
                        console.print("\n no se encontraron documentos para eliminar")
                except Exception as e:
                    console.print(f"\n [red] error al eliminar: {e}[/red]")
        elif choice == "5":
            console.print(f"\n [bold] contar documentos [/bold]")

            try:
                query = console.input("ingrese filtro (opcional, ej {'activo' : true}): ")
                query = eval(query) if query else {}

                count = collection.count_documents(query)
                console.print(f"\n [green] total de documentos: {count}[/green] ")

            except Exception as e:
                console.print(f"\n [red]  error al contar documentos  {e}[/red] ")
        else:
            console.print("\n [red] opcion invalida, intente nuevamente. [/red]")
        console.input("\n precione enter para continuar...")
        console.clea()