from config import get_settings

base_url = get_settings().base_url
print(f'base: {base_url}')

dburl = get_settings().db_url
print(f'db: {dburl}')

