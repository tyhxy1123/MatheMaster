# Unsere LaTeX style guidelines

## Grundlegende Regeln
1. LaTeX-Code immer einrücken. Eingerücken wird stets zwischen `\begin{...}` und `\end{...}`. Es wird mit einem Tab eingerückt.
2. Die Nummerierung sowie Formelnummern (sofern vorhanden) müssen exakt mit der Vorlesung übereinstimmen (nutze `\tag` und `\setcounter`).
3. Alle LaTeX-Warnungen beheben. Nur Warning-free code wird gepusht. 
 (Tipp: Der `\nl`-command kann underfull boxes vermeiden und dennoch optische Leerzeilen erzeugen.)

##  Kleinigkeiten
1. Der `\enter` command wird sparsam verwendet, d.h. nur an Stellen, an denen `\\` nicht funktioniert.
2. Statt `\stackrel` immer `\overset` nutzen. 
3. Statt `$$`, `\[` und `Equation`-Umgebungen (oder ähnliches) sind immer `align*`-Umgebungen zu benutzen.
(Tipp: Dank dem Package `aligned-overset` bietet sich Syntax `\overset{\text{Magie}}&{=}` an, wenn man Code alignen will.)
4. `\item`'s die aus Formeln bestehen sollten mit `aligned`-Umgebungen ausgestattet werden, z. B.

```
\begin{itemize}
	\item $\begin{aligned}
		A=B
	\end{aligned}$
\end{itemize}
```

5. Was definiert wird, wird **fett** gekennzeichnet.
6. Labelnamen für Gleichungen fangen stets mit "eq" an und werden ausschließlich mit `\eqref{eq...}` referenziert.
7. Es wird empfohlen, hinter einem abgeschlossenem (sprachlichen) Satz eine neue Codezeile zu beginnen.
8. Commands etc. werden immer in einer dafür vorgesehenen Datei auslagern (z.B. `commands_ANGA.tex`, oder `commands_Maik.tex`, je nach Zweck).
9. Von `\begin{...}` gefolgten `\end{...}` Befehlen immer durch leere Codezeile trennen (z. B. `\end{theorem}\begin{proof}`).
10. Labels von Sätzen mit Namen müssen diesen Namen enthalten (z.B. `\label{satz7.4DreiecksungleichFuerPros}`).

## Grafiken und Tikz
Grafiken und Tikz-Pictures sind immer grundsätzlich in Unterordner "pics" bzw. "tikz" auszulagern.
Das Einbinden von Grafiken sollte stets die folgende Form haben:
```
\begin{figure}[ht!]
	\begin{center}
		\includegraphics[width=0.75\textwidth]{./pics/grafik1.png}
		\caption{Bildunterschrift}
		\label{AbbTitel}
	\end{center}
\end{figure}
```
Analog für Tikz:
```
\begin{figure}[ht!]
	\begin{center}
		\input{./tikz/tikz.png}
		\caption{Bildunterschrift}
		\label{AbbTitel}
	\end{center}
\end{figure}
```
Wichtig ist, dass die Labels immer mit "Abb" beginnen. Das macht das referenzieren leichter.
