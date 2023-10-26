from django.dispatch import receiver
from django.db.models.signals import post_save
from . models import UserData
from PIL import Image
import pytesseract
import os


@receiver(post_save, sender=UserData)
def create_profile(sender, instance, created, **kwargs):
    if created:
        print('sender',sender)
        print('instance',instance)
        print('instance',instance.sshot)

        # Transforming image to string and printing it!
        text = pytesseract.image_to_string(Image.open(instance.sshot))
        bannedWord = ['CoD','E','UT', 'rr', 'Note', ':', 'If', 'consignee', 'wants', 'the', 'shipment', 'select', 'Delivered', 'else', 'Un-Delivered','Please', 'Enter', 'Otp', 'resent', 'on', 'registered', 'No.',]

        
        new = ' '.join(i for i in text.split() if i not in bannedWord)
        splitted = new.split()

        # for cod parcel
        if 'Amount' in splitted:
            val2 = splitted.index('Amount')
       
            for i in splitted:
                if i.isnumeric():
                    val1 = splitted.index(i)
                            

            raw_final = splitted[val1+1:val2]

            instance.address = " ".join(raw_final)
            instance.save()

        # for prepaid parcel
        elif 'PPD' in splitted:

            for i in splitted:
                if i.isnumeric():
                    val1 = splitted.index(i)

            raw_final = splitted[val1+1:]

            instance.address = " ".join(raw_final)
            instance.save()
            

        
       
        
                

