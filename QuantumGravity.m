%% =========================================================================
% QUANTUM GRAVITY: Unifying the Universe and the Future of Technology
% MATLAB Computational Research Script: QuantumGravity.m
% Authors: Dr. Nathaniel Brooks & Dr. Julian Hayes
% Description:
%   Rigorous numerical evaluation of fundamental Planck-scale quantities,
%   Schwarzschild event horizon scaling, physical length hierarchy,
%   and conceptual models of classical vs. quantized spacetime.
% =========================================================================

function QuantumGravity()
    fprintf('------------------------------------------------------------\n');
    fprintf(' QUANTUM GRAVITY NUMERICAL COMPUTATION PIPELINE\n');
    fprintf(' MATLAB Computational Engine\n');
    fprintf('------------------------------------------------------------\n');

    % 1. FUNDAMENTAL PHYSICAL CONSTANTS (CODATA 2018 / 2022 SI Values)
    c     = 299792458;              % Speed of light in vacuum (m/s)
    G     = 6.67430e-11;            % Newtonian gravitational constant (m^3 kg^-1 s^-2)
    hbar  = 1.054571817e-34;        % Reduced Planck constant (J*s)
    h     = 2 * pi * hbar;          % Planck constant (J*s)
    kB    = 1.380649e-23;           % Boltzmann constant (J/K)
    eV    = 1.602176634e-19;        % Electron volt to Joules (J/eV)
    GeV   = 1e9 * eV;               % Gigaelectronvolt to Joules (J/GeV)
    M_sun = 1.98847e30;             % Solar mass (kg)
    M_earth = 5.9722e24;            % Earth mass (kg)

    % 2. PLANCK SCALE CALCULATIONS
    l_P = sqrt(hbar * G / (c^3));          % Planck length (m)
    t_P = sqrt(hbar * G / (c^5));          % Planck time (s)
    E_P_joules = sqrt(hbar * (c^5) / G);   % Planck energy (J)
    E_P_GeV = E_P_joules / GeV;            % Planck energy (GeV)
    m_P = sqrt(hbar * c / G);              % Planck mass (kg)
    T_P = E_P_joules / kB;                 % Planck temperature (K)
    rho_P = m_P / (l_P^3);                 % Planck density (kg/m^3)

    fprintf('1. Planck Length (l_P)      : %.6e meters\n', l_P);
    fprintf('2. Planck Time (t_P)        : %.6e seconds\n', t_P);
    fprintf('3. Planck Energy (E_P)      : %.6e Joules (%.4e GeV)\n', E_P_joules, E_P_GeV);
    fprintf('4. Planck Mass (m_P)        : %.6e kg\n', m_P);
    fprintf('5. Planck Temperature (T_P) : %.6e Kelvin\n', T_P);
    fprintf('6. Planck Density (rho_P)   : %.6e kg/m^3\n', rho_P);

    % 3. SCHWARZSCHILD RADIUS CALCULATIONS (r_s = 2*G*M / c^2)
    % Mass spectrum spanning 50 orders of magnitude
    log_mass_min = -8;   % ~Planck mass (2.18e-8 kg)
    log_mass_max = 42;   % ~Supermassive Black Hole cluster (1e42 kg)
    mass_array = logspace(log_mass_min, log_mass_max, 500);
    rs_array   = (2 * G * mass_array) ./ (c^2);

    % Reference astronomical and theoretical benchmark objects
    benchmark_names = { ...
        'Planck Mass', ...
        'Micro Black Hole (10^12 kg)', ...
        'Mount Everest (~8e14 kg)', ...
        'Earth', ...
        'Jupiter', ...
        'Solar Mass (1 M_sun)', ...
        'Cygnus X-1 (Stellar BH, 21 M_sun)', ...
        'Sagittarius A* (Milky Way SMBH, 4.3e6 M_sun)', ...
        'M87* (Supermassive BH, 6.5e9 M_sun)', ...
        'TON 618 (Ultramassive BH, 6.6e10 M_sun)' ...
    };

    benchmark_masses = [ ...
        m_P, ...
        1e12, ...
        8.1e14, ...
        M_earth, ...
        1.898e27, ...
        M_sun, ...
        21.2 * M_sun, ...
        4.297e6 * M_sun, ...
        6.5e9 * M_sun, ...
        6.6e10 * M_sun ...
    ];

    benchmark_rs = (2 * G * benchmark_masses) ./ (c^2);
    benchmark_hawking_T = (hbar * (c^3)) ./ (8 * pi * G .* benchmark_masses * kB);

    % Ensure output directories exist
    results_dir = fullfile(pwd, 'results');
    images_dir = fullfile(pwd, 'static', 'images');
    if ~exist(results_dir, 'dir'), mkdir(results_dir); end
    if ~exist(images_dir, 'dir'), mkdir(images_dir); end

    % ---------------------------------------------------------------------
    % PLOT 1: Planck-Scale Physical Constants Dashboard
    % ---------------------------------------------------------------------
    fig1 = figure('Visible', 'off', 'Position', [100, 100, 1200, 800], 'Color', [0.06, 0.08, 0.12]);
    t1 = tiledlayout(2, 2, 'Padding', 'compact', 'TileSpacing', 'compact');
    title(t1, 'Planck-Scale Physical Constants & Quantum Thresholds', ...
        'Color', [0.95, 0.96, 0.98], 'FontSize', 16, 'FontWeight', 'bold');

    % Subplot 1A: Fundamental scales bar plot
    ax1 = nexttile;
    set(ax1, 'Color', [0.09, 0.11, 0.17], 'XColor', [0.7, 0.75, 0.85], 'YColor', [0.7, 0.75, 0.85]);
    scales_val = [log10(l_P), log10(t_P), log10(m_P), log10(E_P_GeV)];
    b1 = bar(scales_val, 'FaceColor', [0.15, 0.55, 0.95], 'EdgeColor', [0.4, 0.75, 1.0]);
    set(ax1, 'XTickLabel', {'log_{10}(l_P [m])', 'log_{10}(t_P [s])', 'log_{10}(m_P [kg])', 'log_{10}(E_P [GeV])'});
    grid on; grid minor;
    ax1.GridColor = [0.2, 0.25, 0.35]; ax1.GridAlpha = 0.6;
    ylabel('Exponent (log_{10} SI/GeV Units)', 'Color', [0.85, 0.9, 0.95]);
    title('Fundamental Planck Dimensions', 'Color', [0.95, 0.96, 0.98]);

    % Subplot 1B: Energy Scale comparison
    ax2 = nexttile;
    set(ax2, 'Color', [0.09, 0.11, 0.17], 'XColor', [0.7, 0.75, 0.85], 'YColor', [0.7, 0.75, 0.85]);
    energy_labels = {'LHC Proton Collision', 'Ultra-High Cosmic Ray', 'Planck Energy (E_P)'};
    energy_gev = [1.36e4, 3e11, E_P_GeV];
    b2 = barh(log10(energy_gev), 'FaceColor', [0.95, 0.45, 0.2], 'EdgeColor', [1.0, 0.65, 0.4]);
    set(ax2, 'YTickLabel', energy_labels);
    xlabel('log_{10}(Energy in GeV)', 'Color', [0.85, 0.9, 0.95]);
    title('Accelerator Frontiers vs. Planck Energy Gap', 'Color', [0.95, 0.96, 0.98]);
    grid on; grid minor;
    ax2.GridColor = [0.2, 0.25, 0.35]; ax2.GridAlpha = 0.6;

    % Subplot 1C: Temperature and Density comparison
    ax3 = nexttile;
    set(ax3, 'Color', [0.09, 0.11, 0.17], 'XColor', [0.7, 0.75, 0.85], 'YColor', [0.7, 0.75, 0.85]);
    temps = [2.7255, 1.5e7, 1e12, T_P];
    temp_labels = {'CMB (Universe)', 'Sun Core', 'Quark-Gluon Plasma', 'Planck Temp (T_P)'};
    bar(log10(temps), 'FaceColor', [0.85, 0.25, 0.65], 'EdgeColor', [1.0, 0.45, 0.85]);
    set(ax3, 'XTickLabel', temp_labels);
    ylabel('log_{10}(Temperature [Kelvin])', 'Color', [0.85, 0.9, 0.95]);
    title('Thermal Scales of the Universe', 'Color', [0.95, 0.96, 0.98]);
    grid on; grid minor;
    ax3.GridColor = [0.2, 0.25, 0.35]; ax3.GridAlpha = 0.6;

    % Subplot 1D: Uncertainty Principle limit
    ax4 = nexttile;
    set(ax4, 'Color', [0.09, 0.11, 0.17], 'XColor', [0.7, 0.75, 0.85], 'YColor', [0.7, 0.75, 0.85]);
    dx = logspace(-36, -30, 200);
    dp = hbar ./ (2 * dx);
    semilogy(dx, dp, 'LineWidth', 2.5, 'Color', [0.2, 0.9, 0.6]);
    hold on;
    xline(l_P, '--r', sprintf('Planck Length (%.2e m)', l_P), 'LineWidth', 2, 'Color', [1.0, 0.3, 0.3]);
    grid on; grid minor;
    ax4.GridColor = [0.2, 0.25, 0.35]; ax4.GridAlpha = 0.6;
    xlabel('\Delta x Position Uncertainty (m)', 'Color', [0.85, 0.9, 0.95]);
    ylabel('\Delta p Momentum Uncertainty (kg\cdotm/s)', 'Color', [0.85, 0.9, 0.95]);
    title('Quantum Uncertainty: \Delta x \cdot \Delta p \geq \hbar/2', 'Color', [0.95, 0.96, 0.98]);

    exportgraphics(fig1, fullfile(images_dir, 'planck_constants_dashboard.png'), 'Resolution', 300);
    exportgraphics(fig1, fullfile(results_dir, 'planck_constants_dashboard.png'), 'Resolution', 300);
    close(fig1);

    % ---------------------------------------------------------------------
    % PLOT 2: Schwarzschild Radius versus Mass
    % ---------------------------------------------------------------------
    fig2 = figure('Visible', 'off', 'Position', [100, 100, 1200, 800], 'Color', [0.06, 0.08, 0.12]);
    ax = axes(fig2);
    set(ax, 'Color', [0.09, 0.11, 0.17], 'XColor', [0.7, 0.75, 0.85], 'YColor', [0.7, 0.75, 0.85]);
    loglog(mass_array, rs_array, 'LineWidth', 3, 'Color', [0.15, 0.65, 1.0], 'DisplayName', 'r_s(M) = 2GM / c^2 (Exact Einstein Metric)');
    hold on;

    % Plot benchmark points
    scatter(benchmark_masses, benchmark_rs, 80, [1.0, 0.8, 0.2], 'filled', 'DisplayName', 'Astrophysical & Theoretical Benchmarks');
    for i = 1:length(benchmark_names)
        text(benchmark_masses(i) * 1.5, benchmark_rs(i), benchmark_names{i}, ...
            'Color', [0.9, 0.92, 0.98], 'FontSize', 9, 'Interpreter', 'none');
    end

    % Highlight Planck Mass / Length intersection
    scatter(m_P, 2 * l_P, 120, [1.0, 0.3, 0.3], 'p', 'filled', 'DisplayName', 'Planck Scale Threshold (M \approx m_P, r_s \approx 2 l_P)');
    yline(l_P, ':g', 'Planck Length l_P', 'LineWidth', 1.8, 'Color', [0.2, 0.9, 0.6]);

    grid on; grid minor;
    ax.GridColor = [0.2, 0.25, 0.35]; ax.GridAlpha = 0.6;
    xlabel('Object Mass M (kg)', 'Color', [0.85, 0.9, 0.95], 'FontSize', 12);
    ylabel('Schwarzschild Radius r_s (m)', 'Color', [0.85, 0.9, 0.95], 'FontSize', 12);
    title('Schwarzschild Event Horizon Radius vs. Mass (Spanning 50 Orders of Magnitude)', ...
        'Color', [0.95, 0.96, 0.98], 'FontSize', 15, 'FontWeight', 'bold');
    legend('Location', 'northwest', 'TextColor', [0.9, 0.92, 0.98], 'Color', [0.12, 0.15, 0.22]);

    exportgraphics(fig2, fullfile(images_dir, 'schwarzschild_radius_vs_mass.png'), 'Resolution', 300);
    exportgraphics(fig2, fullfile(results_dir, 'schwarzschild_radius_vs_mass.png'), 'Resolution', 300);
    close(fig2);

    % ---------------------------------------------------------------------
    % PLOT 3: Black Hole Radius Comparison
    % ---------------------------------------------------------------------
    fig3 = figure('Visible', 'off', 'Position', [100, 100, 1200, 800], 'Color', [0.06, 0.08, 0.12]);
    ax3 = axes(fig3);
    set(ax3, 'Color', [0.09, 0.11, 0.17], 'XColor', [0.7, 0.75, 0.85], 'YColor', [0.7, 0.75, 0.85]);

    bh_display_names = {'Earth Horizon', '1 Solar Mass BH', 'Cygnus X-1', 'Sagittarius A*', 'M87*'};
    bh_rs_values = [ ...
        (2 * G * M_earth) / (c^2), ...
        (2 * G * M_sun) / (c^2), ...
        (2 * G * 21.2 * M_sun) / (c^2), ...
        (2 * G * 4.297e6 * M_sun) / (c^2), ...
        (2 * G * 6.5e9 * M_sun) / (c^2) ...
    ];

    b3 = bar(log10(bh_rs_values), 'FaceColor', [0.2, 0.75, 0.65], 'EdgeColor', [0.4, 0.95, 0.85]);
    set(ax3, 'XTickLabel', bh_display_names);
    ylabel('log_{10}(Schwarzschild Radius [m])', 'Color', [0.85, 0.9, 0.95], 'FontSize', 12);
    title('Comparative Gravitational Radii Across Black Hole Classes', ...
        'Color', [0.95, 0.96, 0.98], 'FontSize', 15, 'FontWeight', 'bold');
    grid on; grid minor;
    ax3.GridColor = [0.2, 0.25, 0.35]; ax3.GridAlpha = 0.6;

    for i = 1:length(bh_rs_values)
        if bh_rs_values(i) < 1
            txt = sprintf('%.2f mm', bh_rs_values(i) * 1000);
        elseif bh_rs_values(i) < 1000
            txt = sprintf('%.2f m', bh_rs_values(i));
        elseif bh_rs_values(i) < 1e9
            txt = sprintf('%.2f km', bh_rs_values(i) / 1000);
        else
            txt = sprintf('%.2f AU', bh_rs_values(i) / 1.496e11);
        end
        text(i, log10(bh_rs_values(i)) + 0.4, txt, 'HorizontalAlignment', 'center', ...
            'Color', [1.0, 0.9, 0.5], 'FontSize', 10, 'FontWeight', 'bold');
    end

    exportgraphics(fig3, fullfile(images_dir, 'black_hole_radius_comparison.png'), 'Resolution', 300);
    exportgraphics(fig3, fullfile(results_dir, 'black_hole_radius_comparison.png'), 'Resolution', 300);
    close(fig3);

    % ---------------------------------------------------------------------
    % PLOT 4: Logarithmic Hierarchy of Physical Scales
    % ---------------------------------------------------------------------
    fig4 = figure('Visible', 'off', 'Position', [100, 100, 1200, 800], 'Color', [0.06, 0.08, 0.12]);
    ax4 = axes(fig4);
    set(ax4, 'Color', [0.09, 0.11, 0.17], 'XColor', [0.7, 0.75, 0.85], 'YColor', [0.7, 0.75, 0.85]);

    scale_names = { ...
        'Planck Length (l_P)', ...
        'GUT Symmetry Scale', ...
        'Higgs/Electroweak Scale', ...
        'Top Quark Limit', ...
        'Proton Radius', ...
        'Hydrogen Atom', ...
        'DNA Helix Width', ...
        'Human Scale (~1.7 m)', ...
        'Earth Radius', ...
        'Solar Radius', ...
        '1 Light Year', ...
        'Milky Way Galaxy', ...
        'Observable Universe' ...
    };

    scale_meters = [ ...
        l_P, ...
        1e-31, ...
        1e-18, ...
        1e-19, ...
        0.84e-15, ...
        0.53e-10, ...
        2.5e-9, ...
        1.7, ...
        6.371e6, ...
        6.96e8, ...
        9.461e15, ...
        1e21, ...
        8.8e26 ...
    ];

    colors = jet(length(scale_meters));
    scatter(1:length(scale_meters), log10(scale_meters), 120, colors, 'filled');
    hold on;
    plot(1:length(scale_meters), log10(scale_meters), '--', 'Color', [0.4, 0.5, 0.65], 'LineWidth', 1.5);
    set(ax4, 'XTick', 1:length(scale_meters), 'XTickLabel', scale_names);
    xtickangle(40);
    ylabel('Characteristic Length Scale: log_{10}(meters)', 'Color', [0.85, 0.9, 0.95], 'FontSize', 12);
    title('Hierarchy of Fundamental Length Scales: From l_P to the Observable Universe (61 Orders of Magnitude)', ...
        'Color', [0.95, 0.96, 0.98], 'FontSize', 14, 'FontWeight', 'bold');
    grid on; grid minor;
    ax4.GridColor = [0.2, 0.25, 0.35]; ax4.GridAlpha = 0.6;

    % Annotate the 61 orders span
    text(2, 20, sprintf('Spans \\Delta \\approx 10^{61} Orders of Magnitude\nPlanck Length: %.2e m\nUniverse Radius: %.2e m', l_P, 8.8e26), ...
        'Color', [0.2, 0.9, 0.6], 'FontSize', 11, 'BackgroundColor', [0.12, 0.15, 0.22]);

    exportgraphics(fig4, fullfile(images_dir, 'length_scale_hierarchy.png'), 'Resolution', 300);
    exportgraphics(fig4, fullfile(results_dir, 'length_scale_hierarchy.png'), 'Resolution', 300);
    close(fig4);

    % ---------------------------------------------------------------------
    % PLOT 5: Conceptual Spacetime Fluctuation Visualization
    % ---------------------------------------------------------------------
    fig5 = figure('Visible', 'off', 'Position', [100, 100, 1200, 700], 'Color', [0.06, 0.08, 0.12]);

    % Subplot 5A: Classical Continuous Spacetime (Einstein Smooth Curvature)
    ax5a = subplot(1, 2, 1);
    set(ax5a, 'Color', [0.09, 0.11, 0.17]);
    [X, Y] = meshgrid(linspace(-5, 5, 50), linspace(-5, 5, 50));
    R = sqrt(X.^2 + Y.^2) + 0.1;
    Z_classical = -2.5 ./ (1 + 0.3 * R.^2); % Smooth gravitational potential well
    mesh(X, Y, Z_classical, 'FaceColor', 'none', 'EdgeColor', [0.2, 0.6, 1.0], 'LineWidth', 1.0);
    hold on;
    scatter3(0, 0, -2.5, 100, [1.0, 0.7, 0.2], 'filled');
    title({'General Relativity: Classical Smooth Spacetime', 'Continuous Riemannian Curvature (G_{\mu\nu} = \kappa T_{\mu\nu})'}, ...
        'Color', [0.95, 0.96, 0.98], 'FontSize', 12);
    xlabel('Spatial Dimension x', 'Color', [0.75, 0.8, 0.9]);
    ylabel('Spatial Dimension y', 'Color', [0.75, 0.8, 0.9]);
    zlabel('Spacetime Curvature g_{00}', 'Color', [0.75, 0.8, 0.9]);
    grid on; ax5a.GridColor = [0.2, 0.25, 0.35]; ax5a.GridAlpha = 0.5;
    view(-30, 45);

    % Subplot 5B: Quantum Spacetime / Wheeler Quantum Foam (Conceptual Simulation)
    ax5b = subplot(1, 2, 2);
    set(ax5b, 'Color', [0.09, 0.11, 0.17]);
    % Add stochastic Planckian metric fluctuations
    rng(42); % Deterministic seed for reproducible scientific visualization
    fluc_high_freq = 0.35 * (sin(3*X) .* cos(3*Y) + sin(6*X) .* sin(6*Y)) + 0.2 * randn(size(X));
    Z_quantum = Z_classical + fluc_high_freq;
    surf(X, Y, Z_quantum, 'EdgeColor', [0.8, 0.3, 0.7], 'FaceAlpha', 0.85);
    colormap(ax5b, turbo);
    title({'Quantum Gravity: Hypothesized Quantum Foam', 'Discrete Planckian Geometric Fluctuations (\Delta g_{\mu\nu} \sim l_P / L)'}, ...
        'Color', [0.95, 0.96, 0.98], 'FontSize', 12);
    xlabel('Planck Scale x / l_P', 'Color', [0.75, 0.8, 0.9]);
    ylabel('Planck Scale y / l_P', 'Color', [0.75, 0.8, 0.9]);
    zlabel('Metric Operator Eigenvalues', 'Color', [0.75, 0.8, 0.9]);
    grid on; ax5b.GridColor = [0.2, 0.25, 0.35]; ax5b.GridAlpha = 0.5;
    view(-30, 45);

    % Annotation emphasizing conceptual non-direct observation
    sgtitle({'Comparative Spacetime Models: Classical Continuum vs. Planckian Quantum Foam', ...
        '[Theoretical Conceptual Model — Not Directly Observed Image of Spacetime]'}, ...
        'Color', [0.95, 0.96, 0.98], 'FontSize', 14, 'FontWeight', 'bold');

    exportgraphics(fig5, fullfile(images_dir, 'spacetime_fluctuations_comparison.png'), 'Resolution', 300);
    exportgraphics(fig5, fullfile(results_dir, 'spacetime_fluctuations_comparison.png'), 'Resolution', 300);
    close(fig5);

    % ---------------------------------------------------------------------
    % 4. EXPORT NUMERICAL RESULTS TO JSON
    % ---------------------------------------------------------------------
    benchmarks_struct = cell(length(benchmark_names), 1);
    for i = 1:length(benchmark_names)
        benchmarks_struct{i} = struct( ...
            'name', benchmark_names{i}, ...
            'mass_kg', benchmark_masses(i), ...
            'schwarzschild_radius_m', benchmark_rs(i), ...
            'hawking_temperature_K', benchmark_hawking_T(i) ...
        );
    end

    scales_struct = cell(length(scale_names), 1);
    for i = 1:length(scale_names)
        scales_struct{i} = struct( ...
            'name', scale_names{i}, ...
            'length_m', scale_meters(i), ...
            'log10_m', log10(scale_meters(i)) ...
        );
    end

    out_data = struct( ...
        'title', 'Quantum Gravity & Planck Scale Numerical Analysis', ...
        'execution_engine', 'MATLAB (Native Engine)', ...
        'execution_timestamp', char(datetime('now', 'Format', 'yyyy-MM-dd HH:mm:ss')), ...
        'scientific_constants', struct( ...
            'speed_of_light_m_s', c, ...
            'gravitational_constant_m3_kg_s2', G, ...
            'reduced_planck_constant_J_s', hbar, ...
            'boltzmann_constant_J_K', kB ...
        ), ...
        'planck_scale', struct( ...
            'planck_length_m', l_P, ...
            'planck_time_s', t_P, ...
            'planck_energy_joules', E_P_joules, ...
            'planck_energy_GeV', E_P_GeV, ...
            'planck_mass_kg', m_P, ...
            'planck_temperature_K', T_P, ...
            'planck_density_kg_m3', rho_P ...
        ), ...
        'schwarzschild_benchmarks', {benchmarks_struct}, ...
        'length_hierarchy', {scales_struct}, ...
        'scientific_limitation', [ ...
            'These calculations demonstrate established physical relationships and mathematical scales. ' ...
            'They do not solve quantum gravity or experimentally prove a particular quantum gravity theory.' ...
        ] ...
    );

    json_str = jsonencode(out_data, 'PrettyPrint', true);
    fid = fopen(fullfile(results_dir, 'quantum_gravity_data.json'), 'w');
    fprintf(fid, '%s', json_str);
    fclose(fid);

    % Duplicate to data/ directory for static distribution
    fid2 = fopen(fullfile(pwd, 'data', 'quantum_gravity_data.json'), 'w');
    fprintf(fid2, '%s', json_str);
    fclose(fid2);

    fprintf('\nMATLAB Computation Complete!\n');
    fprintf('Results saved to results/quantum_gravity_data.json and static/images/\n');
end
