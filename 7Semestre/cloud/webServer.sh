#!/bin/bash

# Intalar o Apache Web Server.
yum update -y
yum install -y httpd

# Iniciar o serviço do Apache e habilitá-lo para iniciar automaticamente na inicialização do sistema.
systemctl start httpd
systemctl enable httpd

# Vamos buscar a informação de qual Availability Zone a instância está rodando e criar um arquivo index.html com essa informação.
TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"`
AVAILABILITY_ZONE=`curl -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/placement/availability-zone`

# Criar o arquivo index.html com a informação da Availability Zone.
cat > /var/www/html/index.html << EOF
<!DOCTYPE html>
<html>
<head>
    <title>Web Server</title>
</head>
<body>
    <h1>Bem-vindo ao meu Web Server!</h1>
    <p>Esta instância está rodando na Availability Zone: $AVAILABILITY_ZONE</p>
</body>
</html>
EOF
