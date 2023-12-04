import websocket
import _thread
import time
import rel

# from websocket import WebSocket

def sendMessageWS(message, chatroom, username):
    ws = websocket.WebSocket()
    ws.connect("ws://127.0.0.1:8000/ws/chat/"+chatroom+"/")
    print("Sending'...")
    ws.send('{"message":"'+message+'", "user":"'+username+'"}')
    print("Sent")
    # print("Receiving...")
    # result = ws.recv()
    # print("Received '%s'" % result)
    ws.close()


class WebsocketClient:
    def on_message(ws, message):
        print(message)

    def on_error(ws, error):
        print(error)

    def on_close(ws, close_status_code, close_msg):
        print("### closed ###")

    def on_open(ws):
        print("Opened connection")

    # if __name__ == "__main__":
    def send(self, message):
        websocket.enableTrace(True)
        ws = websocket.WebSocketApp("wss://api.gemini.com/v1/marketdata/BTCUSD",
                                  on_open=self.on_open,
                                  on_message=self.on_message,
                                  on_error=self.on_error,
                                  on_close=self.on_close)

        ws.run_forever(dispatcher=rel, reconnect=5)  # Set dispatcher to automatic reconnection, 5 second reconnect delay if connection closed unexpectedly
        rel.signal(2, rel.abort)  # Keyboard Interrupt
        rel.dispatch()