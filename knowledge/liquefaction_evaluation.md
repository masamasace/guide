---
title: "液状化判定"
date: "2024-03-22"
---

## 液状化判定の基本的な考え方

現行の判定法の多くは応力法をベースにしている。ここでの応力法とは、繰り返しせん断が作用した際に土の強度が下がった状態において、土の強度と地震力の比によって限界状態の安全率を求める手法。

### 現行の液状化判定手法

- 米国
    - [Idriss and Boulanger (2014)](https://web.archive.org/web/20240821084255/https://www.ce.memphis.edu/7137/PDFs/Notes/i3Boulanger_Idriss_CPT_and_SPT_Liq_triggering_CGM-14-01_20141.pdf)に記載されている手法

### Idriss and Boulanger (2014)の日本語訳と解説

- CSRはCyclic Stress Ratioの略
    - ある深度における最大せん断応力比の65%をCSRと定義
    - 文字式で書くと次のようになる $CSR_{M,\ \sigma'_v}$
        - なぜ65%なのか？
        - Seed and Idriss (1967)の論文によって提案されたもので、そこから使われている。
        - この0.65という値を変えた場合、特定のパラメータの値が変わってくるが、全体を通して同じ値(0.65なり他の値であれ)を使えば、液状化評価手順の最終結果には影響を与えない
            - ほんとうか？これでCSRが変わってくる以上FL値も変わってくるのではないか？
    - 最大せん断応力は、動的応答解析などを用いて計算する必要があるが、入力の時刻歴加速度や正確な地盤情報が必要となるため無理そうだ
        - そのため、地表面の最大加速度を用いて近似的に求めることが多い
        - 式は次のようになる
        $$CSR_{M,\ \sigma'_v} = 0.65\frac{\sigma_v}{\sigma'_{v}}\frac{a_{max}}{g}r_d$$
        - なぜ $\sigma_v$ が分子にくるんだろう？
            - ある深度より上に存在する単位体積当たりの地盤の重量は $\sigma_v$ (N) 
            - よって質量は $\sigma_v/g$ (kg)
            - よって作用する地震慣性力は $\sigma_v/g \times a_{max}$ (N)
                - ここには、次の仮定がある。
                    - 地盤の質量は地表面まで一様に分布している
                    - 地盤の質量は地表面まで一様に加速度を受けている
                - 上記の仮定も考慮して、$r_d$が設定されている。
- CRRはCyclic Resistance Ratioの略
    - CRRはCPTやSPTの貫入抵抗値を上載圧で補正することによって求める。
        - CPTの場合はIdriss and Boulanger, 2008やIdriss and Boulanger, 2010に記載されている式を用いる
    - 上載圧補正係数をかけた $\left(N_1\right)_{60}$は標準大気圧において他の全ての属性が同じであった場合の砂の貫入抵抗値を示す。
        - Maki et al., 2014がもう少し詳しく検討しているっぽい
    - CRRは地震動の継続時間や、有効上載圧($K_\sigma$)による
        - ここからがわからないポイント
            - 継続時間が長いとCRRが低くなるという仮定があるのか？
            - 有効上載圧と水平土圧係数$K_\sigma$の関係がわからない
            - `The correlation for CRR is therefore developed by adjusting the case history CSR values`と書かれているが、なぜthereforeなのか？CRRの補正係数であれば、CRRに対して直接補正をすればよくないか？
    - CRRはもちろん、基礎直下の地盤や斜面上に存在する地盤などがうける静的なせん断応力の影響も受ける。
        - ただケースヒストリーのデータベースは、水平かほぼ水平の地盤に対してのものが多く、この文献では考慮していない
    - 細粒分補正について
        - 本当であれば細粒分の補正は次のような式で書きたい
        $$CRR_{M=7.5,\ \sigma'_v=1\rm{atm}} = f[\left(N_1\right)_{60},\ FC]$$
        - しかし、実際には細粒分含有率が $\left(N_1\right)_{60}$ の増分に影響を与えると仮定して計算を行う。すなわち
        $$\begin{align*}
        CRR_{M=7.5,\ \sigma'_v=1\rm{atm}} &= f[\left(N_1\right)_{60cs}] \\
        \left(N_1\right)_{60cs} &= \left(N_1\right)_{60} + \Delta\left(N_1\right)_{60} \\ 
        \Delta\left(N_1\right)_{60} &= f[FC]
        \end{align*}$$
        - CPTの場合も基本的に先端抵抗値を同様の手法で補正することで求められるが、いくつか代替手法も提案されている。
    