from sqlalchemy import create_engine, inspect

engine = create_engine('sqlite:///C:/JPEM_Git_Main/JPEM/JPEM_Datacamp/data/Chinook.sqlite')

inspector = inspect(engine)

table_names = inspector.get_table_names()
print(table_names)
