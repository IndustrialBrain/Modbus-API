from flask import  Flask, request, jsonify, json
from pyModbusTCP.client import ModbusClient


# Inicia configuração TCP
c = ModbusClient(host="localhost", port=502, unit_id=1, auto_open=True)
# Parametros conexão Modbus
c = ModbusClient()
c.host("localhost")
c.port(502)
c.unit_id(1)
#Configura APP para API
app = Flask(__name__)

#Rota para leitura
@app.route("/read", methods = ['POST'])
def leitura():
     # Abre conexão TCP
    c.open()

    #Leitura de 3 registros a partir do 40001
    regs = c.read_holding_registers(0, 3)
    if regs:
        print(regs)
        #Fecha conexão    
        c.close()
        return jsonify({"40001":regs[0], "40002":regs[1], "40003":regs[2]} )
    else:
        print("read error")
        #Fecha conexão    
        c.close()
        return "Erro na leitura" 


#Rota para Escrita
@app.route("/write", methods = ['POST'])
def escrita():
    # Valores recebidos
    valores = json.loads(request.data)

     # Abre conexão TCP
    c.open()

   #Escreve em 3 registros a partir do 40004. Escrita apenas para demonstrar.
    if c.write_multiple_registers(3, [valores["40004"],valores["40005"],valores["40006"]]):
        print("write ok")
        #Fecha conexão    
        c.close()
        return "escrita OK"
    else:
        print("write error")
        #Fecha conexão    
        c.close()
        return "escrita OK"
    
    
    
