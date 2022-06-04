from django.db import models

# Create your models here.
class Usuario(models.Model):
	id_num=models.AutoField(primary_key=True)
	name=models.CharField(max_length=50)
	apellido=models.CharField(max_length=50)
	cedula=models.CharField(max_length=20)

class Producto(models.Model):
	id_num=models.AutoField(primary_key=True)
	name=models.CharField(max_length=80)
	marca=models.CharField(max_length=50)
	serial=models.CharField(max_length=50)

class Sede(models.Model):
	id_num=models.AutoField(primary_key=True)
	name=models.CharField(max_length=80)

class Almacen(models.Model):
	id_num=models.AutoField(primary_key=True)
	name=models.CharField(max_length=80)

class Depart(models.Model):
	id_num=models.AutoField(primary_key=True)
	name=models.CharField(max_length=80)

class Cargo(models.Model):
	id_num=models.AutoField(primary_key=True)
	name=models.CharField(max_length=80)

class Operador(models.Model):
	id_num=models.AutoField(primary_key=True)
	id_usuario=models.BigIntegerField()
	id_cargo=models.BigIntegerField()
	id_sede=models.BigIntegerField()
	id_depart=models.BigIntegerField()
	fecha_asig=models.CharField(max_length=30)

class equipo_asignado(models.Model):
	id_num=models.AutoField(primary_key=True)
	id_producto=models.BigIntegerField()
	id_operador=models.BigIntegerField()
	status=models.BooleanField()
	cantidad=models.BigIntegerField()

class almacenamiento(models.Model):
	id_num=models.AutoField(primary_key=True)
	id_producto=models.BigIntegerField()
	id_almacen=models.BigIntegerField()
	cantidad=models.BigIntegerField()