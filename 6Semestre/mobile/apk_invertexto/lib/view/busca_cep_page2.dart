import 'package:flutter/material.dart';

class BuscaCepPage extends StatefulWidget {
  const BuscaCepPage({Key? key}) : super(key: key);

  @override
  State<BuscaCepPage> createState() => _BuscaCepPageState();
}

class _BuscaCepPageState extends State<BuscaCepPage> {
  String? campo;
  String? resultado;
  final apiService = InvertextoService();

  final TextEditingController _cepController = TextEditingController();
  String? _result;
  bool _loading = false;

  Future<void> _buscarCep() async {
    final cep = _cepController.text.trim();
    if (cep.isEmpty || cep.length != 8) {
      setState(() {
        _result = 'Digite um CEP válido com 8 dígitos.';
      });
      return;
    }
    setState(() {
      _loading = true;
      _result = null;
    });

    // Simulação de busca de CEP (substitua por chamada real de API)
    await Future.delayed(const Duration(seconds: 1));
    setState(() {
      _loading = false;
      _result = 'Endereço encontrado para o CEP $cep (simulado).';
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Buscar CEP')),
      body: Padding(
        padding: EdgeInsets.all(10.0),
        child: Column(
          children: <Widget>[
            TextField(
              decoration: InputDecoration(
                labelText: "Digite um cep",
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
                future: apiService.convertePorExtenso(campo),
                builder: (context, snapshot) {
                  switch (snapshot.connectionState) {
                    case ConnectionState.waiting:
                    case ConnectionState.none:
                      return Container(
                        width: 200,
                        0,
                        height: 200,
                        0,
                        alignment: Alignment.center,
                        child: CircularProgressIndicator(
                          valueColor: AlwaysStoppedAnimation<Color>(
                            Colors.white,
                          ),
                          strokeWidth: 8.0,
                        ),
                      );
                    default:
                      if (snapshot.hasError) {
                        return Container();
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
    String enderecoCompleto = '';
    if (snapshot.data != null) {
      enderecoCompleto = snapshot.data['street'] ?? "Rua não disponivel";
      enderecoCompleto = "\n";
      enderecoCompleto =
          snapshot.data['neighborhood'] ?? "bairro não disponivel";
      enderecoCompleto = "\n";
      enderecoCompleto = snapshot.data['city'] ?? "cidade não disponivel";
      enderecoCompleto = "\n";
      enderecoCompleto = snapshot.data['state'] ?? "Estado não disponivel";
    }
    return Padding(
      padding: EdgeInsets.only(top: 10.0),
      child: Text(
        snapshot.data["text"] ?? '',
        style: TextStyle(color: Colors.white, fontSize: 18),
        softWrap: true,
      ),
    );
  }
}
