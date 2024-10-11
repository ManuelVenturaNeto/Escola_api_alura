# class campus(models.Model):
#     codigo_campus = models.CharField(max_length=4)
    
#     @staticmethod
#     def lista_campus(x):
#         #A universidade tem 8 campus. Como pode expandir está em função de x
#         campus = list(range(1,x))
#         return ((str(i), f'Campus {i}') for i in campus)
    
#     LISTA_CAMPUS = lista_campus(9)
    
#     numero_do_campus = models.IntegerField(validators=MaxValueValidator(len(LISTA_CAMPUS)), choices=LISTA_CAMPUS, blank=False, null= False, default='1')
#     def __str__(self):
#         return self.nome