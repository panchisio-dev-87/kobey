from supabase import create_client, Client

# 🔧 Configura tus credenciales de Supabase
SUPABASE_URL = "https://thuvedithigvnghchycc.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InRodXZlZGl0aGlndm5naGNoeWNjIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDkwNjA5ODAsImV4cCI6MjA2NDYzNjk4MH0.JRALEFzqUNcRoWmsQiRwIEYikk-4Z7WA8Ren64LnRAw"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)




TABLE_NAME = "mi_coleccion"  # Debe existir en tu base de datos

def supabase_save_or_update_session(data):
    company_base = data.get("company_base")
    if not company_base:
        print("Error: 'company_base' es obligatorio.")
        return

    # Buscar si ya existe
    existing = supabase.table(TABLE_NAME).select("*").eq("company_base", company_base).execute()

    if not existing.data:
        # No existe: insertar todo
        supabase.table(TABLE_NAME).insert(data).execute()
        print(f"Insertado nuevo documento para company_base: {company_base}")
    else:
        # Ya existe: actualizar según lógica
        record_id = existing.data[0]["id"]

        if data.get("error") is None:
            # No hay error: actualizar todos los campos
            update_data = data
        else:
            # Hay error: actualizar solo 'error' y 'timestamp'
            update_data = {
                "error": data.get("error"),
                "timestamp": data.get("timestamp")
            }

        supabase.table(TABLE_NAME).update(update_data).eq("id", record_id).execute()
        print(f"Actualizado documento para company_base: {company_base}")

def supabase_get_all_sessions():
    result = supabase.table(TABLE_NAME).select("*").execute()
    return result.data

def supabase_get_session_by_company_base(company_base):
    result = supabase.table(TABLE_NAME).select("*").eq("company_base", company_base).execute()
    return result.data[0] if result.data else None



