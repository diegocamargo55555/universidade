import nodemailer from 'nodemailer';
import HandlebarsMailTemplate from './HandlebatsMainTemplate';
interface ITemplateVariable{
    [key: string]: string|number;
}
interface IMailContact{
    name: string;
    email: string;
}
interface IParseMailTemplate{
    file: string;
    variables: ITemplateVariable;
}
interface ISendMail{
    to: IMailContact;
    from?: IMailContact;
    subject: string;
    templateData: IParseMailTemplate;
}
export default class EtherealMail{
    static async sendMail({to, from, subject, templateData}: ISendMail): Promise<void>{
        const account = await nodemailer.createTestAccount();
        const mailTemplate = new HandlebarsMailTemplate();
        const transporter = nodemailer.createTransport({
            host: account.smtp.host,
            port: account.smtp.port,
            auth:{
                user: account.user,
                pass: account.pass,
            },
             secure: account.smtp.secure, // importante! usar o valor correto
    
            tls: {
            rejectUnauthorized: false //
            }
        });
        const message = await transporter.sendMail({
            from: {
                name: from?.name || 'Equipe API Vendas',
                address: from?.email || 'equipe_vendas@apivendas.com.br' 
            },
            to: {
                name: to.name,
                address: to.email
            },
            subject,
            html: await mailTemplate.parse(templateData)
        })
        console.log('Message sent: %s', message.messageId);
        console.log('Preview URL: %s', nodemailer.getTestMessageUrl(message));
    }
}