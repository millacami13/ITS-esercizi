class ContactManager:

    def __init__(self, contacts: dict[str, list[str]] = {}):
        
        self.contacts = contacts

    def create_contact (self, name: str, phone_numbers: list[str]) -> dict[str, list[str]]:
        
        if name in self.contacts:
            raise ValueError ("Errore: il contatto esiste già")
        else:
            self.contacts [name] = phone_numbers

            return {name : phone_numbers} #nuovo dizionario che contiene una chiave sola e un valore solo

    def add_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:
        
        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")
        if phone_number in self.contacts[contact_name]:
            raise ValueError ("Errore: il numero di telefono esiste già")
        
        self.contacts[contact_name].append(phone_number)

        return {contact_name: self.contacts[contact_name]}
    
    def remove_phone_number(self, contact_name: str, phone_number: str) -> dict[str, list[str]]:

        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")
        if phone_number not in self.contacts[contact_name]:
            raise ValueError ("Errore: il numero di telefono non è presente.") 

        self.contacts[contact_name].remove(phone_number)

        return {contact_name: self.contacts[contact_name]}   

    def update_phone_number(self, contact_name: str, old_phone_number: str,new_phone_number: str) -> dict[str, list[str]]:

        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")
        if old_phone_number not in self.contacts [contact_name]:
            raise ValueError ("Errore: il numero di telefono non è presente")

        index: int = self.contacts[contact_name].index(old_phone_number)
        self.contacts[contact_name][index] = new_phone_number

        return {contact_name: self.contacts[contact_name]}

    def list_contacts(self) -> list[str]:

        return list(self.contacts.keys())

    def list_phone_numbers(self, contact_name: str) -> list[str]:

        if contact_name not in self.contacts:
            raise ValueError ("Errore: il contatto non esiste")

        return self.contacts[contact_name]

    def search_contact_by_phone_number(self, phone_number: str) -> list[str]:

        contacts_list:list[str] = []

        for contacts, list_contacs in self.contacts.items():
            if phone_number in list_contacs:
                contacts_list.append(contacts)
        if contacts_list == []:
            raise Exception ("Newssun contatto trovato con questo numero di telefono")

        return contacts_list            
