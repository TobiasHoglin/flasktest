#code for streaming


#were to implement the start_stream() function
from stream_test_lib import *
def start_stream():
    picam2 = Picamera2()
    picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
    picam2.start_recording(JpegEncoder(), FileOutput(output))

    try:
        address = ('', 5000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
        return server
    finally:
        picam2.stop_recording()


