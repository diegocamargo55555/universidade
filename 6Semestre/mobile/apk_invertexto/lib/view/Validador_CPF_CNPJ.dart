import 'package:apk_invertexto/service/invertexto_service.dart';
import 'package:flutter/material.dart';

class validadorCPF_CNPJ extends StatefulWidget {
  const validadorCPF_CNPJ({super.key});

  @override
  State<validadorCPF_CNPJ> createState() => _validadorCPF_CNPJState();
}

class _validadorCPF_CNPJState extends State<validadorCPF_CNPJ> {
  String? campo;
  String? resultado;
  final apiService = InvertextoService();
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/imgs/invertexto.png',
              fit: BoxFit.contain,
              height: 40,
            ),
          ],
        ),
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: Icon(
            Icons.arrow_back,
            color: const Color.fromARGB(255, 255, 246, 220),
          ),
        ),
        centerTitle: true,
      ),
      backgroundColor: Colors.black,
      body: Padding(
        padding: EdgeInsets.all(10),
        child: Column(
          children: [
            TextField(
              decoration: InputDecoration(
                labelText: "Digite um CPF ou CNPJ: ",
                labelStyle: TextStyle(color: Colors.white),
                border: OutlineInputBorder(),
              ),
              keyboardType: TextInputType.number,
              style: TextStyle(color: Colors.white, fontSize: 18),
              onSubmitted: (value) {
                setState(() {
                  campo = value;
                });
              },
            ),
            Expanded(
              child: FutureBuilder(
                future: apiService.valida_CPF_CNPJ(campo),
                builder: (context, snapshot) {
                  switch (snapshot.connectionState) {
                    case ConnectionState.waiting:
                    case ConnectionState.none:
                      return Container(
                        width: 200,
                        height: 200,
                        alignment: Alignment.center,
                        child: CircularProgressIndicator(
                          valueColor: AlwaysStoppedAnimation<Color>(
                            Colors.white,
                          ),
                        ),
                      );
                    default:
                      if (snapshot.hasError) {
                        if (campo?.isNotEmpty == true) {
                          return SizedBox(
                            height: 500,
                            width: 1500,
                            child: Column(
                              children: <Widget>[
                                Icon(
                                  Icons.error,
                                  color: Colors.white,
                                  size: 50.0,
                                ),
                                Text(
                                  "Error",
                                  style: TextStyle(
                                    color: Colors.white,
                                    fontSize: 20,
                                  ),
                                ),
                              ],
                            ),
                          );
                        } else {
                          return Container();
                        }
                      } else {
                        return exibeResultado(context, snapshot);
                      }
                  }
                },
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget exibeResultado(BuildContext context, AsyncSnapshot snapshot) {
    String resultado = '';
    if (snapshot.data["formatted"] != null) {
      resultado += snapshot.data["formatted"] + ": ";
    }
    if (snapshot.data["valid"] == true) {
      resultado += "válido";
    } else {
      resultado += "inválido";
    }
    return Padding(
      padding: EdgeInsets.only(top: 10),
      child: Text(
        resultado,
        style: TextStyle(color: Colors.white, fontSize: 18),
      ),
    );
  }
}
