import asyncio
import json


from services import cf

async def main():
    data_dict =await cf.cd_request(method_param='contest.list?gym=false')
    with open('info.json','w') as f:
        f.write(json.dumps(data_dict))

if __name__ == '__main__':
    asyncio.run(main())