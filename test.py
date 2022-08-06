import asyncio

from whatsapie import LocationMessage, MessageGroup, TextMessage, Whatsapie

manager = Whatsapie("EAAF1rnPZCVTsBAMaQZCZAHUDNm1jm6ac1lqZAEXnxVkt3c0MWhQRozNQut2ZC91FbWWx9S7ik8p3Fk47OZCebUAk4S5ZC4MRoAFzpvwqfBIuf3SbDpvOWllPKSOiQfLZAVbTCZBu2G1cZB29qQ0m4vOPHHirWuUrz9Pjw2UdKYQejkWkBjuPMOCS94McohZALlxj2OCy8yGqQD7mszaPa4EmdVkxfKTKZC6lpGPkoZCOOVEE7xgZDZD", "101271475945402", log=True)

group = MessageGroup([TextMessage(body="hello 1"), TextMessage(body="hello 2"), LocationMessage(long="10", lat="10", name="mama", address="oye")], to="917356998597")

async def main():
    await manager.send_group(group)

asyncio.run(main())