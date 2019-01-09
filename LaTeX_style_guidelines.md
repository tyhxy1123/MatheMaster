# LaTeX style guideline
=====================

## 1. Grundlagen
----------
1.1. LaTeX-Code immer einrücken. Eingerücken wird stets zwischen `\begin{...}` und `\end{...}`.
1.2. Die Nummerierung (sofern vorhanden) sowie Formelnummern müssen exakt mit der Vorlesung übereinstimmen (nutze `\tag`).
1.3. Clean-Code: KEINE Warnings! (Tipp: Der `\nl`-command kann underfull boxes vermeiden und dennoch optische Leerzeilen erzeugen.)
1.4. Statt `$$` und Equation-Umgebungen oder ähnliches sind immer `align*`-Umgebungen zu nutzen.

## 2. Kleinigkeiten
----------------
2.1. Den `\enter` command sparsam verwenden! Nur an Stellen, an denen `\\` nicht funktioniert.
2.2. -----
2.3. Statt \stackrel immer `\overset` nutzen. Es bietet sich dank einen speziellen Packages die Syntax `\overset{\text{Magie}}&{=}` an, wenn man Symbole alignen will.
2.4. In Itemize- oder Enumerate-Umgebungen sind stets aligned-Umgebungen zu nutzen, z. B.

`
\begin{itemize}
	\item $\begin{aligned}
		A=B
	\end{aligned}$
\end{itemize}
`

2.5. Was definiert wird, wird fett gekennzeichnet.
2.6. Labelname für Gleichungen fangen stets mit "eq" an und werden ausschließlich mit `\eqref{eq...}` referenziert!
2.7. Pro Zeile höchstens einen (sprachlichen) Satz.
2.8. Commands immer in einer Extra-Datei auslagern (z.B. commands_ANGA.tex, oder commands_Maik.tex, je nach Scope).
2.9. Von `\begin{...}` gefolgten `\end{...}` Befehlen immer durch Leerzeile trennen (z. B. `\end{theorem}\begin{proof}`).
2.10. Labels von Sätzen mit Namen müssen diesen Namen enthalten (z.B. `\label{satz7.4DreiecksungleichFuerPros}`).

## 3. Bilder
---------
Bilder und Tikz-Pictures sind immer grundsätzlich auszulagern in Unterordner "pics" bzw. "tikz".
Zum Einbinden von Bildern immer folgendes Snippet verwenden:

`
\begin{figure}[ht!]
	\begin{center}
		\includegraphics[width=0.75\textwidth]{./pics/Sketch2.png}
		\caption{Bildunterschrift}
		\label{AbbTitel}
	\end{center}
\end{figure}
`

Code Snippet für Tikz-Bikder:

`
\begin{figure}[ht!]
	\begin{center}
		\input{./tikz/tikz.png}
		\caption{Bildunterschrift}
		\label{AbbTitel}
	\end{center}
\end{figure}
`

Wichtig ist, dass die Labels immer mit "Abb" beginnen. Das macht das referenzieren leichter.
