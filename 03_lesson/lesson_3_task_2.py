from smartphone import Smartphone

catalog =[Smartphone('Iphone','15','+7-999-123-45-78'),
          Smartphone('Samsung', 'S8','+7-987-654-32-10'),
          Smartphone('Techno', "Pova 6 neo",'+7-901-234-56-78'),
          Smartphone('Xiaomi', '17 PRo','+7-923-456-78-90'),
          Smartphone('Honor', 'Pura 80', '+7-912-323-45-65')]
for phone in catalog:
    print(phone.phone_brand,'-',phone.phone_model,'.',phone.phone_number)