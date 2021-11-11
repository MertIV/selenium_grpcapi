from server import Server
import module.db.db_action as engine

if __name__ == '__main__':
    engine.create_tables()
    # Server.run()
