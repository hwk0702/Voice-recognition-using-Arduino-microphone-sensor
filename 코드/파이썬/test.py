import serial
import numpy as np
import tensorflow as tf
import playsound

config = tf.ConfigProto()
config.gpu_options.allow_growth = True

X = tf.placeholder(tf.float32, [None, 30, 129, 1])
Y = tf.placeholder(tf.float32, [None, 6])
is_training = tf.placeholder(tf.bool)

L1 = tf.layers.conv2d(X, 32, [3, 3], activation=tf.nn.relu)
L1 = tf.layers.max_pooling2d(L1, [2, 2], [2, 2])
L1 = tf.layers.dropout(L1, 0.7, is_training)

L2 = tf.layers.conv2d(X, 64, [3, 3], activation=tf.nn.relu)
L2 = tf.layers.max_pooling2d(L2, [2, 2], [2, 2])
L2 = tf.layers.dropout(L2, 0.7, is_training)

L3 = tf.contrib.layers.flatten(L2)
L3 = tf.layers.dense(L3, 200, activation=tf.nn.relu)
L3 = tf.layers.dropout(L3, 0.5, is_training)

graph = tf.get_default_graph()

model = tf.layers.dense(L3, 6, activation=None)

saver = tf.train.Saver()
save_file = 'C:/Users/User/PycharmProjects/AIproject2/model/voice.ckpt-1200'

ser = serial.Serial(
    port='/COM3',
    baudrate=115200,
)

data = []
i = 0

tts_add = 'C:/Users/User/PycharmProjects/AIproject2/tts'
tts = ['C:/Users/User/PycharmProjects/AIproject2/tts/강형원.mp3', 'C:/Users/User/PycharmProjects/AIproject2/tts/김가연.mp3', 'C:/Users/User/PycharmProjects/AIproject2/tts/이전우.mp3',' C:/Users/User/PycharmProjects/AIproject2/tts/전한별.mp3', 'C:/Users/User/PycharmProjects/AIproject2/tts/정기평.mp3', 'C:/Users/User/PycharmProjects/AIproject2/tts/정종우.mp3']


print('준비 완료')
while True:
    while True:

        if ser.readable():
            if len(data) <= 32:
                res = ser.readline()
                data.append(res.decode()[:len(res)-1])

            else:
                break

    if len(data) == 33:
        data = data[1:-2]
    elif len(data) == 32:
        data = data[1:-1]
    elif len(data) == 31:
        data = data[0:-1]
    else:
        print('error')

    datas = []

    for line in data:
        d = line.strip().split(',')
        if d[0] != '':
            d = np.array(d, dtype=np.int)
            datas.append(d)


    datas = np.array(datas).reshape((1, 30, 129))
    print(datas)

    with tf.Session(config=config) as sess:
        saver.restore(sess, save_file)
        prediction = tf.argmax(model, 1)
        pre = sess.run(prediction, feed_dict={X: datas.reshape(-1, 30, 129, 1), is_training: False})
        print('예측값: ', pre)

    playsound.playsound(tts[int(pre)], True)

    data = []

    print('준비 완료')
