El servidor permite la entrada de un mayor numero de clientes:
<img width="432" height="72" alt="image" src="https://github.com/user-attachments/assets/a30d2c7b-acba-4f46-bca5-10fab0f3f19f" />

Cuando un cliente envía un mensaje, no solo el servidor hace decode del mensaje, sino que los demás usuarios tienen su propio decodificador para recibir mensajes:
Cliente 1 dice hola:
<img width="106" height="47" alt="image" src="https://github.com/user-attachments/assets/d3fd9a5a-6517-4ddb-bf85-32409aed6b65" />

El servidor recibe el mensaje:
<img width="302" height="32" alt="image" src="https://github.com/user-attachments/assets/137eab7b-92d5-4949-ad00-c372249a0941" />

El servidor reenvia el mensaje a todos los usuarios menos al que envió el mensaje:
<img width="585" height="73" alt="image" src="https://github.com/user-attachments/assets/6411eef8-543a-4e59-b3e6-512f695d6922" />

Perspectiva del otro cliente: 
<img width="307" height="20" alt="image" src="https://github.com/user-attachments/assets/7ca90e49-c090-4801-a59b-73a9cae5bef8" />
