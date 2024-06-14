# provam6_2

## Rodar o projeto

```bash
git clone https://github.com/LuanRM1/provam6_2.git
cd provam6_2
python3 -m venv venv
source venv/bin/activate
pip install ultralytics opencv-python
python3 face_detection.py
```

Espere o programa terminar de rodar e o video será salvo como `processes_la-cabra.mp4`

## Metodo de detecção escolido

O método escolhido foi utilizar um modelo pre treinado chamado [face-Yolov8](https://github.com/akanametov/yolo-face). O Yolo utiliza uma abordagem em que segmenta
a imagem em várias partes, analisa as partes individualmente, e calcula a probabilidade do objeto
desejado estar ali. Contudo, para chegar a um nível aceitável de acertos é necessário criar um dataset robusto,
e realizar diversas rotinas de testes, para que assim o modelo fique plenamente utilizável.

Classificação das Alternativas:

1. CNN:

   - Viabilidade técnica: Alta. São muito eficazes na detecção de faces devido à sua capacidade de aprender características complexas.
   - Facilidade de implementação: Média. Requer mais recursos computacionais.
   - Versatilidade: Alta. Podem ser adaptadas para diversas tarefas.

2. HAAR Cascade:

   - Viabilidade técnica: Média. Funciona bem em muitos cenários, mas pode falhar em condições de iluminação e ângulos variados.
   - Facilidade de implementação: Alta. Disponível em bibliotecas como OpenCV, facilitando a implementação.
   - Versatilidade: Média. Embora eficaz para detecção de faces, é menos adaptável a outras tarefas de visão computacional.

3. Filtros de Correlação Cruzada:

   - Viabilidade técnica: Baixa. Pode funcionar para detecção de padrões simples, mas é menos eficaz para a complexidade de detecção de faces.
   - Facilidade de implementação: Média. Requer compreensão de processamento de sinais.
   - Versatilidade: Baixa. Limitado a tarefas específicas e menos adaptável a variações nas imagens.

4. NN Linear:
   - Viabilidade técnica: Baixa. Redes neurais lineares não têm a capacidade de capturar faces.
   - Facilidade de implementação: Alta. Simples de implementar, mas ineficaz para detecção de faces.
   - Versatilidade: Baixa. Pouco versátil devido à sua simplicidade e limitações técnicas.

Classificação das Alternativas:

1. CNN:

   - CNNs continuam sendo a melhor escolha devido à sua capacidade de aprender características complexas necessárias para a detecção de emoções.

2. HAAR Cascade:

   - Embora menos eficaz para detecção de emoções em comparação com CNNs, ainda pode ser usado como um primeiro passo para detectar faces.

3. Filtros de Correlação Cruzada:

   - Viabilidade ainda baixa, pois a detecção de emoções requer análise detalhada de características faciais que estes filtros não capturam bem.

4. NN Linear:
   - Continua sendo inviável devido à sua incapacidade de lidar com a complexidade da detecção de emoções.

Nenhuma das soluções listadas (HAAR Cascade, CNN, NN Linear, Filtros de Correlação Cruzada) tem a capacidade intrínseca de considerar variações de um frame para outro. Para permitir essa capacidade, pode-se integrar uma abordagem de processamento temporal, como:

- RNN ou LSTM: Essas redes são capazes de capturar dependências temporais, tornando-as adequadas para analisar sequências de frames e detectar mudanças de emoção ao longo do tempo.
