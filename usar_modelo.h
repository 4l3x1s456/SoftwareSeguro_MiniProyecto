#ifndef USAR_MODELO_H
#define USAR_MODELO_H


using namespace mlpack;
using namespace arma;

void usar_modelo_mineriadatos()
{
    // 1. Cargar el modelo entrenado
    mlpack::RandomForest<> rf;
    data::Load("rf_vuln_model.bin", "rf_model", rf);

    // 2. Cargar las características del ejemplo (una fila, mismas columnas que train_features sin label)
    arma::mat exampleData;
    if (!data::Load("example_features.csv", exampleData, true)) // true = transposeIn
    {
        std::cerr << "No se pudo cargar example_features.csv\n";
        return;
    }

    // 3. Obtener prediccion binaria y probabilidades
    arma::Row<size_t> prediction;
    arma::mat probabilities;
    
    // Usar la sintaxis correcta de MLPack para obtener ambos
    rf.Classify(exampleData, prediction, probabilities);

    // 4. Interpretar la prediccion con probabilidades
    if (prediction.n_elem > 0 && probabilities.n_elem > 0)
    {
        double prob_vulnerable = probabilities.n_rows > 1 ? probabilities(1, 0) : 0.0;
        double prob_safe = probabilities.n_rows > 0 ? probabilities(0, 0) : 1.0;
        
        std::cout << "\n=== ANALISIS DE VULNERABILIDAD ===\n";
        std::cout << "Probabilidad de vulnerabilidad: " << (prob_vulnerable * 100) << "%\n";
        std::cout << "Probabilidad de seguridad: " << (prob_safe * 100) << "%\n";
        
        // Alerta automática si probabilidad > 70%
        if (prob_vulnerable > 0.70)
        {
            std::cout << "\nALERTA CRITICA: Alta probabilidad de vulnerabilidad detectada!\n";
            std::cout << "Recomendacion: Revisar inmediatamente el codigo.\n";
        }
        else if (prob_vulnerable > 0.50)
        {
            std::cout << "\nADVERTENCIA: Posible vulnerabilidad detectada.\n";
            std::cout << "Recomendacion: Revisar el codigo por precaucion.\n";
        }
        else
        {
            std::cout << "\nCODIGO SEGURO: Baja probabilidad de vulnerabilidad.\n";
        }
        
        if (prediction[0] == 1)
            std::cout << "\nClasificacion binaria: VULNERABLE\n";
        else
            std::cout << "\nClasificacion binaria: SEGURO\n";
    }
    else
    {
        std::cerr << "No se obtuvo prediccion.\n";
    }
}

#endif // USAR_MODELO_H
