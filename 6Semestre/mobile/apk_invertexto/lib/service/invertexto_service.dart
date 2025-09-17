import 'dart:convert' show json;
import 'dart:io';

import 'package:http/http.dart' as http show get;

class InvertextoService {
  final String _token = "21560|wSAoGEyeVD7ZJ4YsVet5zSPLwBSYjokZ";

  Future<Map<String, dynamic>> convertePorExtenso(
    String? valor,
    String? moeda,
  ) async {
    try {
      final uri = Uri.parse(
        "https://api.invertexto.com/v1/number-to-words?token=${_token}&number=${valor}&language=pt&currency=${moeda}",
      );
      final response = await http.get(uri);
      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Erro ${response.statusCode}: ${response.body}');
      }
    } on SocketException {
      throw Exception('Erro de conexão com a internet');
    } catch (e) {
      rethrow;
    }
  }

  Future<Map<String, dynamic>> buscaCEP(String? valor) async {
    try {
      final uri = Uri.parse(
        "https://api.invertexto.com/v1/cep/${valor}?token=${_token}",
      );
      final response = await http.get(uri);
      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Erro ${response.statusCode}: ${response.body}');
      }
    } on SocketException {
      throw Exception("Erro de conexão com a internet");
    } catch (e) {
      rethrow;
    }
  }

  Future<Map<String, dynamic>> valida_CPF_CNPJ(String? valor) async {
    try {
      final uri = Uri.parse(
        'https://api.invertexto.com/v1/validator?token=$_token&value=${valor} ',
      );
      final response = await http.get(uri);
      if (response.statusCode == 200) {
        return json.decode(response.body);
      } else {
        throw Exception('Erro ${response.statusCode} : ${response.body}');
      }
    } on SocketException {
      throw Exception('Sem conexão com a internet');
    } catch (e) {
      rethrow;
    }
  }
}
