
import smtplib
from email.message import EmailMessage

def submit_email(temperature_three_days, average_all_days_temperature):
    EMAIL_ADDRESS = 'email@gmail.com'
    EMAIL_PASSWORD = 'senha'

    mail = EmailMessage()
    mail['Subject'] = 'Weather Summary'
    mensagem = ''' 
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100;0,300;0,400;0,500;0,700;0,900;1,100;1,300;1,400;1,500;1,700;1,900&display=swap" rel="stylesheet">
        <title>Document</title>
    </head>
    <body style="font-family: Roboto, sans-serif;">
        <main>
            <header 
            style="margin-top: 2rem;"
            ><strong style="font-size: 1.4rem;">Your weather forecast has arrived!</strong></header>
            <div style="padding: 3rem;width: 38rem;" 
            class="content">
                <p style="
                    margin-bottom: 0;
                    background-color: #fdf8f3;
                    padding: 1rem;
                    border-radius: 5px 5px 0 0;
                    text-decoration: underline;
                "
                >Hello, I'm here to deliver the weather forecast for the next 3 days. <br/>
                <div
                class="table">
                    <div style="
                    background-color: #fdf8f3;
                    padding: 1rem;
                    border-radius: 5px 5px 0 0;
                    width: 100%;
                    "  class="day-1">
                        <p> <strong>{0}<strong> The maximum temperature will be <strong>{1}<strong>F, while the minimum will be <strong>{2}<strong>F.</p>
                        <p>The weather condition is forecasted to be <strong>{3}<strong></p>
                    </div>
                    <div style="
                    background-color: #fdf8f3;
                    padding: 1rem;
                    width: 100%;
                "  class="day-2">
                        <p><strong>{4}<strong> The maximum temperature will be <strong>{5}<strong>F, while the minimum will be <strong>{6}<strong>F.</p>
                        <p>The weather condition is forecasted to be <strong>{7}<strong></p>
                    </div>
                    <div style="
                    background-color: #fdf8f3;
                    padding: 1rem;
                    width: 100%;
                    border-radius: 0 0 5px 5px;
                "  class="day-3">
                        <p><strong>{8}<strong> The maximum temperature will be <strong>{9}<strong>F, while the minimum will be <strong>{10}<strong>F.</p>
                        <p>The weather condition is forecasted to be <strong>{11}<strong></p>
                    </div>

                    <p style="
                        background-color: #fdf8f3;
                        margin-top: 0;
                        padding: 1rem;
                        border-radius: 0 0 5px 5px;
            " class="average">The forecasted average for the next 3 days is <strong>{12}<strong>°F.</p>
                </div>
            <p class="more-informations">All the information was obtained from the website: https://www.msn.com/en-us/weather/forecast/in-S%C3%A3o-Paulo,Brazil. Visit it for more information.</p>
                                
            </p>
            </div>
        </main>
    </body>
    </html>
    '''.format(
        temperature_three_days[0][0],
        temperature_three_days[0][1],
        temperature_three_days[0][2],
        temperature_three_days[0][3],

        temperature_three_days[1][0],
        temperature_three_days[1][1],
        temperature_three_days[1][2],
        temperature_three_days[1][3],
        
        temperature_three_days[2][0],
        temperature_three_days[2][1],
        temperature_three_days[2][2],
        temperature_three_days[2][3],

        average_all_days_temperature,
    )
    mail['From'] = EMAIL_ADDRESS
    mail['To'] = 'email@gmail.com'
    mail.add_header('Content-Type', 'text/html')
    mail.set_payload(mensagem.encode('utf-8'))

    # Enviar o email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as email:
        email.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        email.send_message(mail)
