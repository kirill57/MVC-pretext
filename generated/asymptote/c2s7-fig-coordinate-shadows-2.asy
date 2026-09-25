usepackage("amsmath");

texpreamble("
\newcommand{\R}{\mathbb{R}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Cplx}{\mathbb{C}}
\newcommand{\vect}[1]{\mathbf{#1}}
\newcommand{\zerovec}{\mathbf{0}}
\newcommand{\pd}[2]{\frac{\partial #1}{\partial #2}}
\newcommand{\pdmix}[3]{\frac{\partial^{2} #1}{\partial #2 \, \partial #3}}
\newcommand{\norm}[1]{\left\lVert #1 \right\rVert}
\newcommand{\abs}[1]{\left\lvert #1 \right\rvert}
\newcommand{\dform}{\mathrm{d}}
\newcommand{\grad}{\operatorname{grad}}
\newcommand{\divg}{\operatorname{div}}
\newcommand{\curl}{\operatorname{curl}}
\newcommand{\Hess}{\operatorname{Hess}}
\newcommand{\Image}{\operatorname{Im}}
\newcommand{\Kernel}{\operatorname{Ker}}
\newcommand{\spn}{\operatorname{span}}
\newcommand{\sgn}{\operatorname{sgn}}
\newcommand{\inner}[2]{\langle #1, #2 \rangle}
\newcommand{\Arg}{\operatorname{Arg}}
\newcommand{\lt}{<}
\newcommand{\gt}{>}
\newcommand{\amp}{&}
");


        import three;
        size(13cm);
        currentprojection=orthographic(7,-9,6);

        triple o=(0,0,0), u=(2,1,3), v=(1,4,0), w=u+v;
        triple uxy=(2,1,0), vxy=v, wxy=(3,5,0);
        triple uyz=(0,1,3), vyz=(0,4,0), wyz=(0,5,3);
        triple uzx=(2,0,3), vzx=(1,0,0), wzx=(3,0,3);

        pen xyedge=rgb(0.13,0.48,0.27)+linewidth(0.9pt);
        pen yzedge=rgb(0.77,0.34,0.09)+linewidth(0.9pt);
        pen zxedge=rgb(0.48,0.27,0.70)+linewidth(0.9pt);
        pen spaceedge=rgb(0.12,0.29,0.62)+linewidth(1.2pt);

        // Each shadow is the coordinate projection of the same four vertices.
        path3 xy=o--uxy--wxy--vxy--cycle;
        path3 yz=o--uyz--wyz--vyz--cycle;
        path3 zx=o--uzx--wzx--vzx--cycle;
        path3 space=o--u--w--v--cycle;
        draw(surface(xy), rgb(0.29,0.70,0.41)+opacity(0.35));
        draw(surface(yz), rgb(0.96,0.56,0.23)+opacity(0.35));
        draw(surface(zx), rgb(0.64,0.46,0.82)+opacity(0.35));
        draw(surface(space), rgb(0.32,0.54,0.90)+opacity(0.27));

        // Projection segments are parallel to the coordinate omitted by each plane.
        pen xydash=xyedge+linetype("4 3")+opacity(0.7);
        pen yzdash=yzedge+linetype("4 3")+opacity(0.7);
        pen zxdash=zxedge+linetype("4 3")+opacity(0.7);
        draw(u--uxy, xydash); draw(w--wxy, xydash);
        draw(u--uyz, yzdash); draw(v--vyz, yzdash); draw(w--wyz, yzdash);
        draw(u--uzx, zxdash); draw(v--vzx, zxdash); draw(w--wzx, zxdash);

        draw(xy, xyedge); draw(yz, yzedge); draw(zx, zxedge);
        draw(space, spaceedge);
        draw(o--(3.7,0,0), gray(0.45), Arrow3);
        draw(o--(0,5.7,0), gray(0.45), Arrow3);
        draw(o--(0,0,3.8), gray(0.45), Arrow3);
        label("$x$", (3.7,0,0), 2E);
        label("$y$", (0,5.7,0), 2N);
        label("$z$", (0,0,3.8), 2N);

        draw(o--u, spaceedge+linewidth(1.5pt), Arrow3);
        draw(o--v, rgb(0.70,0.22,0.12)+linewidth(1.5pt), Arrow3);
        label("$\mathbf u$", u, 2E);
        label("$\mathbf v$", v, 2N);
        label("$xy: +7$", (1.6,2.7,0), 2S);
        label("$yz: -12$", (0,2.8,1.6), 2W);
        label("$zx: +3$", (1.6,0,1.6), 2E);
        dot(o); dot(w, spaceedge);
        