# from asyncio.windows_events import NULL
from cmath import e
from flask import Flask, request, jsonify, render_template, url_for, redirect
import rsa
import random
import string

import mysql.connector
app = Flask(__name__)


def opendb():
    global mydb, cursor
    mydb = mysql.connector.connect(
        user='root',
        password='',
        database='rsa_db',
        host='127.0.0.1'
    )
    cursor = mydb.cursor()


def closedb():
    global mydb, cursor
    cursor.close()
    mydb.close()


@app.route("/")
def index():

    # opendb()
    # cursor.execute('SELECT * FROM enkripsi')
    # result = []
    # for id, kunci_id, enkripsi_img, enkripsi_text  in cursor.fetchall():
    #     result.append((id, kunci_id, enkripsi_img, enkripsi_text))
    # closedb()
    # return render_template('dashboard/index.html', result=result)
    return render_template('rsa_text_new/index.html')

# START Generate Key


@app.route("/generate-key")
def generate_key():
    if request.method == 'GET':
        return render_template('generate_key/index.html')
    elif request.method == 'POST':
        opendb()
        upload_file = request.files.getlist("file[]")
        filename = []
        for x in upload_file:
            name = []
            img = cv2.imdecode(np.fromstring(
                x.read(), np.uint8), cv2.IMREAD_UNCHANGED)
            filename = secure_filename(x.filename)

            name = filename.split('_')
            if name[2] == "1.jpg" or name[2] == "1.png":
                _target = 1
            else:
                _target = 0
            data = histogram(img)

            glcm = extract_feature(img)

            # data = hsv(img)
            dataa = (filename, str(data[6]), str(data[7]), str(data[8]), str(data[3]), str(
                data[4]), str(data[5]), str(data[0]), str(data[1]), str(data[2]), str(glcm[0]),
                str(glcm[1]), str(glcm[2]), str(glcm[3]), str(
                    glcm[4]), str(glcm[5]), str(glcm[6]), str(glcm[7]),
                str(glcm[8]), str(glcm[9]), str(glcm[10]), str(glcm[11]), str(glcm[12]), str(glcm[13]), str(glcm[14]), str(glcm[15]), _target)

            # dataa = (filename, str(data[0]), str(data[1]), str(data[2]), str(data[3]), str(
            #     data[4]), str(data[5]), str(data[6]), str(data[7]), str(data[8]), _target, 0, 0)

            cursor.execute(
                '''insert into latih(name,r_a,r_b,r_c,g_a,g_b,g_c,b_a,b_b,b_c, contrast_0, energy_0, homogenity_0, entropy_0, contrast_45, energy_45, homogenity_45, entropy_45, contrast_90, energy_90, homogenity_90, entropy_90, contrast_135, energy_135, homogenity_135, entropy_135,target)
                values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s')''' % dataa
            )
            mydb.commit()
        closedb()
        return render_template('generate_key/index.html')

# END Generate Key


@app.route("/rsa-text")
def rsa_text():
    return render_template('rsa_text/index.html')


@app.route("/rsa-text-new", methods=['GET', 'POST'])
def rsa_text_new():
    if request.method == 'GET':
        return render_template('rsa_text_new/index.html', menu='rsa_text_new')
    elif request.method == 'POST':
        # INSERT KUNCI
        opendb()
        text = request.form['plain_text']
        img = request.form['plain_text']

        letters = string.ascii_letters
        kunci_id = ''.join(random.choice(letters) for i in range(10))

        # data array
        data = (kunci_id, text, img,
                request.form['public_key'], request.form['private_key'])

        cursor.execute(
            '''insert into kunci(id,text,img,public_key, private_key)
            values('%s','%s','%s','%s','%s')''' % data
        )
        mydb.commit()
        closedb()

        # INSERT ENRKIPSI
        opendb()
        enkripsi_text = request.form['enkripsi']

        letters = string.ascii_letters
        enkrip_id = ''.join(random.choice(letters) for i in range(10))

        # data array
        data_enkripsi = (enkrip_id, kunci_id, enkripsi_text)

        cursor.execute(
            '''insert into enkripsi(id,kunci_id, enkripsi_text)
            values('%s','%s','%s')''' % data_enkripsi
        )
        mydb.commit()
        closedb()
        # INSERT DEKRIPSI
        opendb()
        dekripsi_text = request.form['dekripsi']

        letters = string.ascii_letters
        dekripsi_id = ''.join(random.choice(letters) for i in range(10))

        # data array
        data_dekripsi = (dekripsi_id, enkrip_id, dekripsi_text)

        cursor.execute(
            '''insert into dekripsi(id,enkripsi_id, dekripsi)
            values('%s','%s','%s')''' % data_dekripsi
        )
        mydb.commit()
        closedb()

    return render_template('rsa_text_new/index.html')


@app.route("/rsa-image-new", methods=['GET', 'POST'])
def rsa_image_new():
    if request.method == 'GET':
        return render_template('rsa_image_new/index.html', menu='rsa_image_new')
    elif request.method == 'POST':
        # INSERT KUNCI
        opendb()
        text = request.form['plain_text']
        img = request.form['plain_text']

        letters = string.ascii_letters
        kunci_id = ''.join(random.choice(letters) for i in range(10))

        # data array
        data = (kunci_id, text, img,
                request.form['public_key'], request.form['private_key'])

        cursor.execute(
            '''insert into kunci(id,text,img,public_key, private_key)
            values('%s','%s','%s','%s','%s')''' % data
        )
        mydb.commit()
        closedb()

        # INSERT ENRKIPSI
        opendb()
        enkripsi_img = request.form['enkripsi']

        letters = string.ascii_letters
        enkrip_id = ''.join(random.choice(letters) for i in range(10))

        # data array
        data_enkripsi = (enkrip_id, kunci_id, enkripsi_img)

        cursor.execute(
            '''insert into enkripsi(id,kunci_id, enkripsi_img)
            values('%s','%s','%s')''' % data_enkripsi
        )
        mydb.commit()
        closedb()
        # INSERT DEKRIPSI
        opendb()
        dekripsi_img = request.form['dekripsi']

        letters = string.ascii_letters
        dekripsi_id = ''.join(random.choice(letters) for i in range(10))

        # data array
        data_dekripsi = (dekripsi_id, enkrip_id, dekripsi_img)

        cursor.execute(
            '''insert into dekripsi(id,enkripsi_id, dekripsi_img)
            values('%s','%s','%s')''' % data_dekripsi
        )
        mydb.commit()
        closedb()

    return render_template('rsa_image_new/index.html')


@app.route("/rsa-image")
def rsa_image():
    return render_template('rsa_image/index.html', menu='rsa_image')


@app.route("/generate", methods=['POST'])
def generate():
    p = request.form['p']
    q = request.form['q']

    rsa_s = rsa.rsa(int(p), int(q))
    rsa_s.setN()
    rsa_s.setM()
    rsa_s.setE()
    rsa_s.setD()

    data = dict([('n', rsa_s.n), ('m', rsa_s.m),
                ('e', rsa_s.e), ('d', rsa_s.d)])

    return jsonify(data)


@app.route("/enkripsi", methods=['POST'])
def enkripsi():
    e = request.form['public_key']
    n = request.form['nilai_n']
    text = request.form['plain_text']
    plainText = [int(ord(c)) for c in text]
    cipherText = [int(pow(s, int(e), int(n))) for s in plainText]

    data = {
        "plain_text_ascii": plainText,
        "decrypt": cipherText
    }

    return jsonify(data)


@app.route("/decrypt", methods=['POST'])
def decrypt():
    d = request.form['private_key']
    n = request.form['nilai_n_decrypt']
    text = request.form['cipher_text']
    ciphertext = text.split(' ')

    plain_text_ascii = [int(pow(int(s), int(d), int(n))) for s in ciphertext]
    plainText = [chr(c) for c in plain_text_ascii]

    data = {
        "plain_text_ascii": plain_text_ascii,
        "plaintext": plainText
    }

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
