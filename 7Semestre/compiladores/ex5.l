%{
#include <stdio.h>
%}

DIGITO  [0-9]

%%

[ \t\n]                 { }

\([1-9]{2}\)\ 9?[0-9]{4}-[0-9]{4} { printf("Telefone: %s\n", yytext); }

97[89]-[0-9]{1,5}-[0-9]{1,7}-[0-9]{1,7}-[0-9] { printf("ISBN: %s\n", yytext); }

({DIGITO}{1,3}\.){3}{DIGITO}{1,3} { printf("IP: %s\n", yytext); }

(http|https|ftp):\/\/[a-zA-Z0-9\-\.]+\.[a-zA-Z]{2,}(:[0-9]+)?(\/[a-zA-Z0-9\-\._\?\,\'\/\\\+&%\$#\=~]*)? { printf("URL: %s\n", yytext); }

. { }

%%

int yywrap() { return 1; }

int main() {
    yylex();
    return 0;
}