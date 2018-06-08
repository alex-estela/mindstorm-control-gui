# add following function in /var/www/web_api/MSWeb.py then run sudo service MSWeb restart:
# in case of errors logs are in /var/tmp/webapi.out

@app.route("/setmotordegrees", methods=['POST', 'OPTIONS'])
@crossdomain(origin='*')
def setmotordegrees():
    try:
        direction = request.form["direction"]
        position = psc.BBM1.pos()
        if direction == 'ahead':
            if position < -20:
                psc.BBM1.runDegs(45,100,True,False)
            elif position > 20:
                psc.BBM1.runDegs(-45,100,True,False)
            else:
                pass
        elif direction == 'left':
            if position < -20:
                pass
            elif position > 20:
                psc.BBM1.runDegs(-90,100,True,False)
            else:
                psc.BBM1.runDegs(-45,100,True,False)
        elif direction == 'right':
            if position < -20:
                psc.BBM1.runDegs(90,100,True,False)
            elif position > 20:
                pass
            else:
                psc.BBM1.runDegs(45,100,True,False)
    except Exception as e:
        pass
    return "1"
