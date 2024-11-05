## Modelo de crescimento exponencial com saturação para ajuste de curvas

<!--<div style="text-align: justify;">-->

### 1. Introdução:
Esse repositório aborda sobre o programa **_esf.py_** que realiza ajustes de curvas para todos os dados experimentais que possam vir a se comportar como um crescimento exponencial com saturação.

Tal programa pode ser utilizado para ajuste de dados experimentais do regime de caregamento em capacitores, dados experimentais de ensaios de absorção de umidade ao ar de materiais hidrofílicos avançados, ajuste de dados na *fase log* (fase B) em diante, para estudo de dinâmica de populações, etc.

### 2. Modelo exponencial

A equação principal usada no modelo é:

$$f(t) = A(1-e^{-t/t_{0}})$$

Onde,

 $$ f:\mathbb{R}_{\ge 0} \to \mathbb{R}_{\ge 0}$$ 
 
O domínio da função $f$ é $\mathbb{R}_{\ge 0}$, ou seja, $t \in [0, +\infty)$  

Os parâmetros $t_{0}$ e $A$ são condições de contorno usadas de acordo com a natureza do problema abordado. $t_{0}$ trata-se de uma constante que controla a taxa de crescimento da função e $A$, o valor limite ou valor máximo assintótico que a função $f(t)$ pode atingir à medida que $t \to +\infty$

</div>

### 3. Ajustes dos dados experimentais (módulo _curve_fit_)

<div style="text-align: justify;">

O ajuste usado neste projeto foi com o auxílio do módulo [_curve_fit_](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.curve_fit.html#scipy.optimize.curve_fit) da biblioteca [_scipy.optimize_ ](https://docs.scipy.org/doc/scipy/reference/optimize.html), que possui uma série de métodos de otimização. Neste projeto o método usado foi o _Trust Region Reflective_ ([_method = 'trf'_](https://docs.scipy.org/doc/scipy/reference/generated/scipy.optimize.least_squares.html#scipy.optimize.least_squares)), um método robusto para problemas com limites e que nos retornam um Erro Final (Custo = 4.8223) e Número de Iterações (8 iterações) menores para este problema. 

O método de otimização _Trust Region Reflective_ tem os seguintes objetivos:

1. Minimizar um problema de mínimos quadrados dentro de uma região de confiança;
2. Resolver um problema quadrático restrito em cada iteração
3. Atualizar a região de confiança com base no sucesso da aproximação.

<div>
   
Para tal, a função de custo utilizada é:

$$f(\mathbf{x}) = \frac{1}{2} \sum_{i=1}^{n} r_i(\mathbf{x})^2$$

onde:

- $x \in \mathbb{R}^{n}$ é o vetor de parâmetros à serem ajustados;
- $r_{i}(x)$ representa os resíduos para cada $i$ amostra.

Tal método busca por uma solução $x$ dentro de uma região de confiança ($\Delta$). Essa região é uma vizinhança em torno do ponto atual em que, localmente, o modelo é considerado confiável. Conforme o ajuste progride, essa região é atualizada em cada iteração para encontrar o $x$ que minimize a função $f(x)$

Para cada passo de atualização de $x$, o problema é aproximado usando uma expansão de Taylor de primeira ordem dos resíduos e de forma iterativa para $p$ (passo da atualização de $x$), visto na seguinte equação:

$$\min_p \| J(x) p + r(x) \|^2 \quad \text{sujeito a} \quad \| p \| \leq \Delta$$

Onde:

- $J(x)$ é o Jacobiano dos resíduos $r(x)$ em relação ao vetor de parâmetros $x$;
- $p$ é o vetor de deslocamento que minimiza o custo quadrático localmente;
- $\Delta$ é o raio da região de confiança.
   
De forma que após resolver o problema quadrático para $p$ dentro da região de confiança, o próximo ponto é atualizado com:

$$x_{novo} = x + p$$

### 4. Características do programa < **_esf.py_** >

- Traça os gráficos dos dados brutos presentes no arquivo _.csv_;
- Permite escolher uma coluna específica de dados para  realizar o ajuste;
- Traça o gráfico de pontos com os dados brutos escolhidos e o gráfico de linha do ajuste desses dados brutos;
- No gráfico, mostra a legenda dos dados brutos, bem como os valores de $A$ e $t_{0}$ ajustados;
- Mostra no terminal o Erro Final (custo), o número de iterações, o Jacobiano da última iteração e a covariância estimada dos parâmetros.

### 5. Requisitos

1. Atualização do sistema:

```bash
$ sudo apt update && sudo apt upgrade
```

2. Instalação das bibliotecas necessárias:
   
```bash
$ pip3.10 install numpy matplotlib pandas scipy
```

3. Execute o programa com seu arquivo _.csv_ onde os números decimais sejam com pontos e separados por vírgulas no mesmo diretório do programa:

```bash
$ python3.10 esf.py
```
### 6. Autor

Este script foi desenvolvido por [Pojucan](https://linkedin.com/in/pojucan). Você pode entrar em contato com o autor através do [seu perfil](https://github.com/pojucan) no GitHub.

### 7. Licença

Este script é distribuído sob a Licença GNU AGPL. Consulte o arquivo [LICENSE](https://www.gnu.org/licenses/gpl-3.0.html) para obter mais detalhes.

### 8. Possíveis melhoramentos

- Obter o coeficiente de determinação ($R^{2}$)
- Obter o coeficiente de determinação ajustado ($R^{2}_{ajus}$)
- Obter o erro padrão da estimativa ($S$)





