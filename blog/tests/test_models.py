from django.contrib.auth.models import User
from django.test import TestCase
from blog.models import Publicacion

class PublicacionModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        autor = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
        Publicacion.objects.create(autor = autor, titulo = 'Titulo publicacion',
                                   texto = 'Texto de prueba de la publicación')
        pass


    def test_titulo_label(self):
        publicacion=Publicacion.objects.get(id=1)
        field_label = publicacion._meta.get_field('texto').verbose_name
        self.assertEquals(field_label,'texto')

    def test_titulo_max_length(self):
        publicacion=Publicacion.objects.get(id=1)
        max_length = Publicacion._meta.get_field('titulo').max_length
        self.assertEquals(max_length,100)

    def test_fechacreacion_label (self):
        publicacion = Publicacion.objects.get(id=1)
        field_label = publicacion._meta.get_field('fechacreacion').verbose_name
        self.assertEquals(field_label,'Creado')

    