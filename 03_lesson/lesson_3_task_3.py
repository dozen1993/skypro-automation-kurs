from address import Address
from mailing import Mailing

address1 = Address('117312', 'Москва', 'Вавилова','17', '43')
address2 = Address('195927', 'Санкт-Петербург', 'Жукова', '123', '1213')
mail_to = Mailing( address1, address2, 454.43 ,'123456789RU')

print('Отправление', mail_to.track, 'из', mail_to.from_address, 'в', mail_to.to_address,'.', 'Стоимость:', mail_to.cost)