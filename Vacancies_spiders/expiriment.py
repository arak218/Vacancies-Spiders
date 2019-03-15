import csv

headers = {'Header1', 'Header2', 'Header3', 'Header4', 'Header5', 'Header6', 'Header7', 'Header8', 'Header9',
           'Header10', 'Header11', 'Header12', 'Header13', 'Header14', 'Header15', 'Header16', 'Header17',
           'Header18', 'Header19', 'Header20', 'Header21', 'Header22', 'Header23', 'Header24', 'Header25',
           'Header26', 'Header27', 'Header28', 'Header29', 'Header30', 'Header31', 'Header32', 'Header33',
           'Header34', 'Header35', 'Header36', 'Header37', 'Header38', 'Header39', 'Header40', 'Header41',
           'Header42', 'Header43', 'Header44', 'Header45', 'Header46', 'Header47', 'Header48', 'Header49',
           'Header50', 'Header51', 'Header52', 'Header53', 'Header54', 'Header55'}
data = ['Data1', 'Data2', 'Data3', 'Data4', 'Data5', 'Data6', 'Data7', 'Data8', 'Data9', 'Data10', 'Data11',
        'Data12', 'Data13', 'Data14', 'Data15', 'Data16', 'Data17', 'Data18', 'Data19', 'Data20', 'Data21',
        'Data22', 'Data23', 'Data24', 'Data25', 'Data26', 'Data27', 'Data28', 'Data29', 'Data30', 'Data31',
        'Data32', 'Data33', 'Data34', 'Data35', 'Data36', 'Data37', 'Data38', 'Data39', 'Data40', 'Data41',
        'Data42', 'Data43', 'Data44', 'Data45', 'Data46', 'Data47', 'Data48', 'Data49', 'Data50', 'Data51',
        'Data52', 'Data53', 'Data54']

with open('eggs.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(headers)
    writer.writerow(data)
