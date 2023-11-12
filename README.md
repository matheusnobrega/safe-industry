# safe-industry
Inteligência artificial utilizada para classificação de sinais de diferentes dispositivos que se conversam através do software de mensageria RabbitMQ. Os dispositivos são redundantes e no momento em que os sinais são detectados como defeituosos pela IA, o sistema principal deixa de funcionar para dar lugar ao redundante.

A redundância na prática é de software. Dois programas que possuem a mesma finalidade são escritos por pessoas distintas sem interação. Os dispositivos são servidores web projetados usando o framework Flask para Python. Assim que o programa se encontra como defeituoso ele é finalizado e o NGINX se encarrega de fazer o balanceamento de carga para o servidor redundante.
