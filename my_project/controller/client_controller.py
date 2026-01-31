from my_project.service.client_service import ClientService

class ClientController:
    def __init__(self):
        self.service = ClientService()

    def get_all(self):
        return self.service.get_all()
    
    def get_by_id(self, client_id):
        return self.service.get_by_id(client_id)

    def create(self, data):
        return self.service.create(data)

    def update(self, client_id, data):
        return self.service.update(client_id, data)

    def delete(self, client_id):
        return self.service.delete(client_id)
    
    def get_stats(self, client_id):
        return self.service.get_client_stats(client_id)
    
    def get_sql_stats(self, client_id):
        return self.service.get_sql_stats(client_id)
        
    def copy_dynamic(self):
        return self.service.trigger_cursor_copy()