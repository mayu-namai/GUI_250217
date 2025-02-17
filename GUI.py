#変更後：評価実験用 0217版

from flask import Flask, render_template, request, jsonify
import os
import application_setting

app = Flask(__name__)

# キャッシュを無効化する設定を追加
app.config.from_object(application_setting)

@app.route('/')
def index():
    # Get list of character and stage images
    characters = os.listdir(os.path.join('static', 'ccfs'))
    stages = os.listdir(os.path.join('static', 'csfs'))

    # ヴィネットイラストの一覧を取得
    vignette_images = os.listdir(os.path.join('static', 'outputs'))

    # 最初のヴィネットイラストをセット（なければ NO_IMAGE_PATH）
    vignette_image = f"/static/outputs/{vignette_images[0]}" if vignette_images else application_setting.NO_IMAGE_PATH

    print(f"Selected vignette_image: {vignette_image}")

    return render_template('index_250217.html', 
                           characters=characters, 
                           stages=stages, 
                           vignette_images=vignette_images, 
                           vignette_image=vignette_image)

@app.route('/complete_selection', methods=['POST'])
def complete_selection():
    data = request.json
    vignette_image_url = data.get('vignette_image')

    # vignette_image のファイル名だけ取得
    vignette_filename = os.path.basename(vignette_image_url)
    vignette_image_path = os.path.join('static', 'outputs', vignette_filename)  # ここを chX_stY.png に変更

    # 画像が存在しない場合は NO_IMAGE_PATH を適用
    if not os.path.exists(vignette_image_path):
        print(f"⚠️ File not found: {vignette_image_path}, using NO_IMAGE_PATH")  # ✅ デバッグ
        vignette_image_url = application_setting.NO_IMAGE_PATH
    else:
        print(f"✅ Found vignette image: {vignette_image_url}")  # ✅ デバッグ

    return jsonify({'status': 'success', 'vignette_image': vignette_image_url})
    
def display_web():
    app.run(host='0.0.0.0', port=5000)

display_web()