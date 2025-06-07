import asyncio
import pdu
from quic_stream import EchoQuicConnection, QuicStreamEvent

async def game_stream_server(conn:EchoQuicConnection):
    while True:
        msg:QuicStreamEvent = await conn.receive()
        datagram = pdu.Datagram.from_bytes(msg.data)

        print(f"[srv] Received {datagram.data} input from user")

        stream_id = msg.stream_id

        resp = datagram.to_bytes()
        resp_evnt = QuicStreamEvent(stream_id, resp, False)

        await conn.send(resp_evnt)