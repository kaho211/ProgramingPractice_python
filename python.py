import math

#角度の範囲を初期化
min_angle = 0
max_angle = 360
increase_angle = 15

#角度を15°ずつ表示
for a in range (min_angle, max_angle, increase_angle): 
    #それぞれの値を少数第四位まで表示
    sin = round(math.sin(math.radians(a)), 4) 
    cos = round(math.cos(math.radians(a)), 4)
    tan = round(math.tan(math.radians(a)), 4)
    
    #角度と計算結果を出力
    print(f"[角度：{a}°]") 
    print(f"sin{a}°は、{sin}")
    print(f"cos{a}°は、{cos}")
    
    #tanの処理（定義域でない場合があるため）
    if a in [90, 270]:
        print(f"tanの定義域ではありません")
    else:
        print(f"tan{a}°は、{tan}")