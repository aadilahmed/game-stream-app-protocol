from typing import Coroutine,Callable, Optional

# Class that defines a new quic stream event
class QuicStreamEvent():
    def __init__(self, stream_id, data, end_stream):
        self.stream_id = stream_id
        self.data = data
        self.end_stream = end_stream

# Class that defines coroutine objects for quic connections   
class EchoQuicConnection():
    def __init__(self, send:Coroutine[QuicStreamEvent, None, None], 
                 receive: Coroutine[None, None, QuicStreamEvent],
                 close:Optional[Callable[[], None]], 
                 new_stream:Optional[Callable[[], int]]):
        self.send = send
        self.receive = receive
        self.close = close
        self.new_stream = new_stream