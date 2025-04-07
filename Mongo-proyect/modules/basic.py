# Importacion de modulos necesarios
from rich.console import Console    # Modulo para mejorar la presentacion en consola
from rich.table import Table    # Modulo para crear tablas en consola
from rich.panel import Panel    # Modulo para crear paneles decorativos

# Creacion de una instancia de Console para la interfaz
console = Console()

def run(db):
    """
    Modulo de conceptos basicos de MongoDB.

    Args:
        db: Instancia de base de datos MongoDB.
        
    Este modulo permite:
        - Explorar comandos basicos de MongoDB.
        - Ver estadisticas de la base de datos.
        - Gestionar base de datos y colecciones.
        - Aprender operaciones fundamentales.
    """
    console.print(Panel.fit(" [bold cyan]Conceptos basicos de MongoDB[/bold cyan]"))
    
    while True:
        # Mostrar menu de operaciones basicas
        table = Table(title="Operaciones basicas", show_header = True)
        table.add_column("Opcion", style="cyan")
        table.add_column("Comando", style="green")
        table.add_column("Descripcion", style="white")
        
        # Agregar opciones al menu
        table.add_row("1", "db.help()", "Mostrar ayuda de comandos de la bases de datos")
        table.add_row("2", "db.stats()", "Mostrar estadisticas de la base de datos")
        table.add_row("3", "show dbs", "Listar todas las bases de datos")
        table.add_row("4", "use <db>", "Cambiar a otra base de datos")
        table.add_row("5", "db.dropDatabase()", "Eliminar la base de datos actual")
        table.add_row("6", "db.createCollection()", "Crear una nueva coleccion")
        table.add_row("7", "show collections", "Listar colecciones en la base de datos actual")
        table.add_row("8", "db.<col>.drop()", "Eliminar una coleccion")
        table.add_row("0", "volver", "Regresar al menu principal")
        
        console.print(table)
        
        choice = console.input("\n + Selecciona una operacion para ejecutar (0-8): ")
        
        if choice == "0":
            break
        
        elif choice == "1":
            # help() - Mostrar informacion de ayuda sobre comandos de MongoDB
            console.print("\n[bold]Ejemplo de db.help():[/bold]")
            console.print("""
            Este comando muestra todos los metodos disponibles para manipular la base de datos.
            
            [yellow]Uso[/yellow]
            > db.help()
            
            [yellow]Comandos comunes:[/yellow]
            - db.adminCommand(nameOrDocument) - Ejecuta comandos en la base de datos admin.
            - db.aggregate([pipeline], {options})- Realiza operaciones de agregacion.
            - db.auth(username, password) - Autenticacion en la base de datos.
            - db.createCollection(name, options) - Crea una nueva coleccion.
            - db.createUser(user) - Crea un nuevo usuario.
            - db.currentOp() - Muestra operaciones en curso.
            - db.dropDatabase() - Elimina la base de datos actual.
            - db.eval() -Ejecuta codigo javaScript.
            - db.fsyncLock() - Bloquea la base de datos para backup.
            - db.fsyncUnlock() - Desbloquea la base de datos.
            - db.getCollection(name) - Obtiene una coleccion.
            - db.getLogComponents() -Obtiene niveles de log.
            - db.getMongo() - Obtiene la conexion de MongoDB.
            - db.getname() - Obtiene el nombre de la base de datos actual.
            - db.getPrevError() - Obtiene errores previos.
            - db.getProfilingLevel() - Obtiene el nivel de profiling.
            - db.getProfilingStatus() - Obtiene el estado de profiling.
            - db.getReplicationInfo() - Obtiene info de replicacion.
            - db.getsiblingDB(name) - Obtiene otra base de datos sin cambiar la actual.
            - db.help() - Muestra esta ayuda.
            - db.hostInfo() - Muestra info del host.
            - db.isMaster() - Verifica si es el nodo primario.
            - db.killOp(opid) - Termina una operacion.
            - db.listCommands() - Lista todos los comandos.
            - db.Logout() - Cierra la sesion actual.
            - db.printCollectionStats() - Imprime estadisticas de la coleccion.
            - db.printReplicationInfo() - Informacion de replicacion.
            - db.printShardingStatus() - Estado del sharding.
            - db.printSlaveReplicationInfo() - Info de replicacion secundaria.
            - db.repairDatabase() - Repara la base de datos.
            - db.resetError() - Resetea errores previos.
            - db.runCommand(cmdObj) - Ejecuta un comando de BD.
            - db.serverStatus() - Estado del servidor.
            - db.setlogLevel(level, component) - Establece nivel de log.
            - db.setProfilingLevel(level, slowms) - Establece el nivel de profiling.
            - db.shutdownServer() - Apaga el servidor.
            - db.stats() - Estadisticas de la base de datos.
            - db.version() - Version de MongoDB.
            """)
        
        elif choice == "2":
            # stats() - Obtener estadisticas de la base de datos actual
            console.print("\n[bold]Ejemplo de db.stats():[/bold]")
            try:
                # command() - Metodo para ejecutar comandos de administracion
                stats = db.command("dbstats")
                
                result_table = Table(title="Estadisticas de la base de datos")
                result_table.add_column("Metrica", style="cyan")
                result_table.add_column("Valor", style="green")
                
                # Agregar metricas importantes con descripciones
                metrics = {
                    "db": "Nombre de la base de datos",
                    "collections": "Numero total de colecciones",
                    "views": "Numero de vistas",
                    "objects": "Numero total de documentos",
                    "avgObjSize": "Tamaño promedio de documentos (bytes)",
                    "dataSize": "Tamaño total de datos (bytes)",
                    "storageSize": "Tamaño en disco (bytes)",
                    "indexes": "Numero total de indices",
                    "indexSize": "Tamaño total de indices (bytes)",
                    "totalSize": "Tamaño total (datos + indices)",
                    "scaleFactor": "Factor de escale para metricas",
                }
                
                for key, desc in metrics.items():
                    if key in stats:
                        value = stats[key]
                        if isinstance(value, (int, float)):
                            if key.endswith("Size"):
                                # Convertir bytes a formato legible
                                value = format_bytes(value)
                        result_table.add_row(f"{key} ({desc})", str(value))
                        
                console.print(result_table)
            except Exception as e:
                console.print(f"\n [red]Error al obtener estadisticas: {e}[/red]")
                
        elif choice == "3":
            # list_database_name() - Listar todas las bases de datos
            console.print("\n[bold]Ejemplo de show dbs:[/bold]")
            try:
                dbs = db.client.list_database_names()
                
                db_table = Table(title="Bases de datos disponibles")
                db_table.add_column("Nombre", style="cyan")
                db_table.add_column("Tamaño", style="green")
                
                for db_name in dbs:
                    # Obtener estadisticas de cada base de datos
                    size = db.client[db_name].command("dbstats")["dataSize"]
                    db_table.add_row(db_name, format_bytes(size))
                    
                console.print(db_table)
            except Exception as e:
                console.print(f"\n [red]Error al listar bases de datos: {e}[/red]")
                
        elif choice == "4":
            # Cambiar a otra base de datos
            console.print("\n[bold]Ejemplo de use <database>:[/bold]")
            db_name = console.input(" Ingresa el nombre de la base de datos a cambiar: ")
            try:
                new_db = db.client[db_name]
                # Intentar una operacion para verificar acceso
                new_db.command("ping")
                console.print(f"\n [green]Cambiado a la base de datos: '{db_name}'[/green]")
                
                # Mostrar colecciones en la nueva base de datos
                cols = new_db.list_collection_names()
                if cols:
                    col_table = Table(title=f"Colecciones en '{db_name}'")
                    col_table.add_column("Nombre", style="cyan")
                    col_table.add_column("Documentos", style="green")
                    
                    for col in cols:
                        count = new_db[col].count_documents({})
                        col_table.add_row(col, str(count))
                        
                    console.print(col_table)
                else:
                    console.print(f"\n La base de datos '{db_name}' no tiene colecciones.")
                    
            except Exception as e:
                console.print(f"\n [red]Error al cambiar de base de datos: {e}[/red]")
        
        elif choice == "5":
            # drop_database() - Eliminar la base de datos actual
            console.print("\n[bold]Ejemplo de db.dropDatabase():[/bold]")
            confirm = console.input(" ¿Estas seguro de eliminar la base de datos '{db.name}'? (s/n): ")
            
            if confirm.lower() == "s":
                try:
                    db.client.drop_database(db.name)
                    console.print(f"\n [green]Base de datos '{db.name}' eliminada correctamente.[/green]")
                except Exception as e:
                    console.print(f"\n [red]Error al eliminar la base de datos: {e}[/red]")
            else:
                console.print("\n Operacion cancelada.")
        
        elif choice == "6":
            # create_collection() - Crear una nueva coleccion
            console.print("\n[bold]Ejemplo de db.createCollection():[/bold]")
            name = console.input(" Nombre de la nueva coleccion: ")
            
            try:
                # Verificar si la coleccion ya existe
                if name in db.list_collection_names():
                    console.print(f"\n [yellow]La coleccion '{name}' ya existe.[/yellow]")
                else:
                    db.create_collection(name)
                    console.print(f"\n [green]Coleccion '{name}' creada correctamente.[/green]")
                    
                    # Mostrar opciones avanzadas disponibles
                    console.print("""
                    [yellow]Opciones disponibles para create_collection():[yellow]
                    - capped: Boolean - Coleccion de tamaño fijo
                    - size: Number - Tamaño maximo en bytes
                    - max: Number - Numero maximo de documentos
                    - validator: Document - Reglas de validacion
                    - validationLevel: String - Nivel de validacion
                    - validationAction: String - Accion al validar
                    """)
            except Exception as e:
                    console.print(f"\n [red]Error al crear la coleccion: {e}[/red]")
                    
        elif choice == "7":
            # list_collection_names() - Listar colecciones
            console.print("\n[bold]Ejemplo de show collections:[/bold]")
            try:
                collections = db.list_collection_names()
                
                if collections:
                    col_table = Table(title="Colecciones en la base de datos actual")
                    col_table.add_column("Nombre", style="cyan")
                    col_table.add_column("Documentos", style="green")
                    col_table.add_column("Tamaño", style="yellow")
                    col_table.add_column("Indices", style="magenta")
                    
                    for col_name in collections:
                        # Obtener estadisticas de la coleccion
                        stats = db.command("collStats", col_name)
                        col_table.add_row(
                            col_name, 
                            str(stats["count"]),
                            format_bytes(stats["size"]),
                            str(len(stats["indexSizes"]))
                            )
                        
                    console.print(col_table)
                else:
                    console.print("\n No hay colecciones en esta base de datos.")
            except Exception as e:
                console.print(f"\n [red]Error al listar colecciones: {e}[/red]")
                
        elif choice == "8":
            # drop() - Eliminar una coleccion
            console.print("\n[bold]Ejemplo de db.<col>.drop():[/bold]")
            collections = db.list_collection_names()
            
            if not collections:
                console.print("\n No hay colecciones para eliminar.")
            else:
                # Mostrar colecciones disponibles
                col_table = Table(title="Colecciones disponibles")
                col_table.add_column("#", style="cyan")
                col_table.add_column("Nombre", style="green")
                col_table.add_column("Documentos", style="yellow")
                
                for i, col_name in enumerate(collections, 1):
                    count = db[col_name].count_documents({})
                    col_table.add_row(str(i), col_name, str(count))
                    
                console.print(col_table)
                
                # Solicitar coleccion a eliminar
                col_choice = console.input("\n Seleccione la coleccion a eliminar (numero): ")
                try:
                    idx = int(col_choice) - 1
                    if 0 <= idx < len(collections):
                        col_name = collections[idx]
                        confirm = console.input(f" ¿Estas seguro de eliminar la coleccion '{col_name}'? (s/n): ")
                        
                        if confirm.lower() == "s":
                            db[col_name].drop()
                            console.print(f"\n [green]Coleccion '{col_name}' eliminada correctamente.[/green]")
                        else:
                            console.print("\n Operacion cancelada.")
                    else:
                        console.print("\n [red]Opcion invalida.[/red]")
                except ValueError:
                    console.print("\n [red]Por favor, ingrese un numero valido.[/red]")
                except Exception as e:
                    console.print(f"\n [red]Error al eliminar la coleccion: {e}[/red]")
            
        else:
            console.print("\n [red]Opcion invalida. Intente nuevamente.[/red]")
            
        console.input("\n Presione Enter para continuar...")
        console.clear()
        
def format_bytes(size):
    """
    Formatea un tamaño en bytes a una cadena legible.

    Args:
        size: Tamaño en bytes.

    Returns:
        str: Tamaño formateado (ej: '1.23 MB')
    """
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} PB"