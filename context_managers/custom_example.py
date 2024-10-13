class DatabaseConnection:
    def __enter__(self):
        print("Connecting to the database")
        self.conn = self._connect_to_database()
        return self.conn

    def __exit__(self,exc_type, exc_value, traceback):
        print("exc_type",exc_type)
        print("exc_value",exc_value)
        print("traceback",traceback)
        print("Disconnecting from the database")
        self.conn.close()

    def _connect_to_database(self):
        # Placeholder for database connection logic
        class Connection:
            def close(self):
                print("Connection closed")
        return Connection()

with DatabaseConnection() as db:
    print(db)
    raise ValueError



