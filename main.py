import pdfkit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    config = pdfkit.configuration(wkhtmltopdf=r"C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe")

    s = """<!DOCTYPE html>
        <html>
        <head>
        <meta charset="UTF-8">
        <style>
            table, td, th {
              border: 1px;
            }
            
            #table1 {
              border-collapse: collapse;
              border-color: black;
            }
            
            #table2 {
              border: 1px solid black;
              border-collapse: collapse;
              border-color: black;
            }
            
            footer {
                position: absolute;
                bottom: 1;
                width: 100%;
                height: 100px;    
                text-align: center;
            }
            
        </style>
        </head>
        
       <h1 align='center'><strong>Sample PDF file from HTML</strong></h1>
       <br></br>
       <body>
       <table id="table1">
        <div>
               <tr>
                    <td><p>Solicitante:</p></td> <td width=400px> </td> <td>Data da Solicitação:</td> <td> </td>
               </tr>
               <tr>
                    <td><p>Centro de Custo:</p></td> <td width=400px> </td> <td>Telefone:</td> <td> </td>
               </tr>
               <tr>
                    <td><p>Responsável: </p></td> <td width=400px> </td> <td>e-Mail:</td> <td> </td>
               </tr>
        </div>
       </table>
       <br></br>
       <table id="table2" align='center'>
            <thead>
               <tr align='center'>
                    <td width=80px><p>Item</p></td> <td width=100px>Quantidade</td> <td width=100px>Unidade</td> <td width=300px>Descricao do Material</td> <td width=100px>Valor</td> <td width=100px>Total</td>
               </tr>
            </thead>
               <tr align='center'>
                    <td><p>1</p></td> <td>3</td> <td>Cx</td> <td>Caneta Azul</td> <td>1.00</td> <td>3.00</td>
               </tr>
               <tr align='center'>
                    <td><p>2</p></td> <td>1</td> <td>Cx</td> <td>Caneta Preta</td> <td>1.00</td> <td>1.00</td>
               </tr>
       </table>
       <br></br>
       <table id="table1">
            <tr><td><h2><strong>Justificativa</strong></h1></td></tr>
            <tr><td>____________________________________________________________________________________________________________</td></tr>
            <tr><td>____________________________________________________________________________________________________________</td></tr>
            <tr><td>____________________________________________________________________________________________________________</td></tr>
       </table>
        <br></br>
        <br></br>
    </body>
        <footer>
          rodapé da pagina
        </footer>
       """


    #nome = str(input('Insira seu nome: '))
    pdfkit.from_string(s, output_path="new_file.pdf", configuration=config)


