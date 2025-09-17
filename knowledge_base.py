from difflib import SequenceMatcher

class SmartKnowledgeBase:
    def __init__(self):
        self.qa_pairs = [
            {
                "question_patterns": [
                    "qué es el comercio internacional",
                    "definición de comercio internacional"
                ],
                "answer": "El comercio internacional se refiere al intercambio de bienes y servicios entre países, lo que permite a las economías especializarse y beneficiarse mutuamente.",
                "confidence": 0.9
            },
            {
                "question_patterns": [
                    "pasos para exportar",
                    "cómo exportar por primera vez"
                ],
                "answer": "Para exportar necesitas: 1) Investigación de mercado, 2) Adaptación del producto, 3) Documentación, 4) Logística y transporte. Para más detalles, visita nuestro blog.",
                "confidence": 0.9
            },
            {
                "question_patterns": [
                    "gracias",
                    "te lo agradezco"
                ],
                "answer": "¡De nada! Es un placer ayudarte con tus preguntas sobre comercio internacional.",
                "confidence": 0.9
            },
            {
                "question_patterns": [
                    "cómo puedo empezar un negocio en Perú",
                    "qué tipo de empresa puedo crear en Perú",
                    "persona natural o jurídica en Perú, ¿cuál es mejor para mi negocio?",
                    "requisitos para abrir una empresa en Perú",
                    "diferencias entre persona natural y jurídica para negocios",
                    "ventajas y desventajas de ser persona natural o jurídica"
                ],
                "answer": "Para iniciar un negocio en Perú, puedes optar por ser una Persona Natural con Negocio o una Persona Jurídica. La elección depende de factores como el tamaño de tu negocio, la reputación que buscas, tu acceso a créditos y la necesidad de separar tus bienes personales de los empresariales.\n\n• Como Persona Natural:\nEres un individuo que ejerce derechos y cumple obligaciones a título personal. Asumes todas las obligaciones de tu negocio, lo que implica que respondes con tu patrimonio y bienes personales por las deudas u obligaciones que pudiera contraer la empresa (responsabilidad ilimitada).\nTe conviene elegir esta opción si vas a iniciar negocios pequeños como bodegas, juguerías, peluquerías, zapaterías, bazares, entre otros. También es adecuada si realizas actividades comprendidas en el Nuevo Régimen Único Simplificado (Nuevo RUS) o si tus clientes van a ser principalmente personas, no empresas. Se recomienda si tu exposición al riesgo ante posibles deudas u obligaciones con terceros es manejable considerando tu patrimonio personal.\n\n• Como Persona Jurídica:\nTe conviene si necesitas mayor reputación en el mercado y quieres tener clientes más grandes o importantes (empresas). Facilita el acceso a créditos o préstamos en bancos y entidades financieras en mejores condiciones. Te permite asegurarte de que, si algo sale mal en tu negocio, se afecten los fondos o bienes de la empresa, no tus bienes personales. Es conveniente si piensas que necesitarás que ingresen inversionistas o más socios, ya que es más fácil transferir participaciones. También es la opción preferible si piensas vender tu negocio o disolverlo después de un tiempo. Las formas comunes de Persona Jurídica incluyen la Sociedad Anónima (SA), Sociedad Comercial de Responsabilidad Limitada (SRL), Sociedad Anónima Cerrada (SAC) o Empresa Individual de Responsabilidad Limitada (EIRL). Para más información, visita este enlace: https://www.gob.pe/263-abrir-o-hacer-negocio",
                "confidence": 0.95
            },
            {
                "question_patterns": [
                    "proceso para crear una empresa en Perú",
                    "requisitos para formar una sociedad en Perú",
                    "pasos para registrar mi negocio como persona jurídica",
                    "cómo formalizar una empresa en Perú",
                    "trámites para establecer una compañía en Perú",
                    "constitución de MYPE en Perú"
                ],
                "answer": "Para constituir una empresa como Persona Jurídica en Perú, se deben seguir los siguientes pasos, muchos de los cuales pueden gestionarse a través de la Plataforma Sistema de Intermediación Digital (SID - SUNARP):\n1. Búsqueda y Reserva de Nombre en la SUNARP: Es altamente recomendable para facilitar la inscripción en el Registro de Personas Jurídicas.\n2. Elaboración del Acto Constitutivo (Minuta): Es un documento esencial donde los miembros manifiestan su voluntad de constituir la empresa.\n3. Abono de Capital y Bienes: Se recomienda un monto mínimo de S/ 1,000.00 para abrir una cuenta bancaria.\n4. Elaboración de la Escritura Pública: Con el Acto Constitutivo y el abono de capital, se acude a una notaría.\n5. Inscripción en Registros Públicos (SUNARP): La notaría se encarga del trámite. La Persona Jurídica existe legalmente a partir de esta inscripción.\n6. Inscripción y Activación del RUC para Persona Jurídica: Al constituirse la empresa a través del SID - SUNARP, la Sunarp incluirá un número de RUC inactivo en la ficha de inscripción. Es responsabilidad del representante legal activarlo.",
                "confidence": 0.95
            },
            {
                "question_patterns": [
                    "regímenes de importación en Perú",
                    "cómo importar mercancías a Perú",
                    "importar productos a Perú: límites de valor FOB",
                    "trámites de aduana para importar",
                    "despacho simplificado de importación vs. importación para el consumo",
                    "importa fácil o envíos de entrega rápida, ¿cuándo usar?",
                    "qué régimen de aduana me corresponde por el valor de mi importación?"
                ],
                "answer": "En Perú, los regímenes para el ingreso de mercancías (importación) se diferencian principalmente por el valor FOB (valor de la mercancía entregada a bordo del transporte designado por el comprador en el puerto de embarque) del envío. Conocer estos límites te ayudará a elegir el procedimiento adecuado. Los principales regímenes son:\n1. Envíos Postales – Importa Fácil (Serpost): valor FOB no debe ser mayor a US$ 2,000.00 por envío.\n2. Envíos de Entrega Rápida (Courier): valor FOB máximo es de US$ 2,000.00 por envío.\n3. Despacho Simplificado de Importación: valor FOB máximo es de US$ 2,000.00 por envío.\n4. Importación para el Consumo: Es para mercancías cuyo valor FOB sea mayor a los US$ 2,000.00. El trámite lo debe realizar obligatoriamente un agente de aduana.",
                "confidence": 0.95
            },
            {
                "question_patterns": [
                    "requisitos para importar mercancías a Perú",
                    "pasos para la Importación para el Consumo",
                    "documentos necesarios para importar a Perú",
                    "proceso aduanero de importación en Perú",
                    "cómo se paga la importación de productos en Perú",
                    "agente de aduanas para importar"
                ],
                "answer": "La Importación para el Consumo es el régimen aduanero que permite el ingreso de mercancías al territorio aduanero para su uso o venta, una vez que se han cumplido todas las formalidades y pagos.\n\n• Requisitos del Importador: El dueño o consignatario debe contar con su número de RUC activo y tener la condición de 'habido'. Es obligatorio contratar un agente de aduana para mercancías con valor FOB mayor a US$ 2,000.00.\n• Consideraciones sobre la Mercancía: No deben ser prohibidas y las restringidas deben contar con un documento de control. Se debe realizar la clasificación arancelaria del producto (código de 10 dígitos) para determinar los tributos aplicables.\n• Procedimiento General:\n1. Numeración de la Declaración Aduanera de Mercancías (DAM): El agente de aduanas solicita la destinación aduanera de forma electrónica.\n2. Transmisión de Documentos Sustentatorios: Se adjuntan documentos digitalmente como la factura, documento de transporte, seguro y otros documentos de control.\n3. Revisión Documentaria o Reconocimiento Físico: El sistema asigna un canal de control: Verde, Naranja o Rojo.\n4. Pago de Tributos: Los derechos arancelarios, demás tributos a la importación y recargos se pagan en moneda nacional al tipo de cambio venta vigente.\n5. Obtención del Levante: Una vez que el pago es validado y la revisión se completa, la SUNAT otorga el levante para que dispongas libremente de tus mercancías.",
                "confidence": 0.95
            },
            {
                "question_patterns": [
                    "cómo se clasifica mi producto para importar en Perú",
                    "arancel de aduanas Perú",
                    "impuestos a la importación Perú",
                    "qué es la subpartida nacional",
                    "calcular impuestos de importación en Perú",
                    "derechos aduaneros Perú",
                    "determinación de la base imponible para importaciones"
                ],
                "answer": "La correcta clasificación arancelaria de tu mercancía es un paso fundamental, ya que de ella dependen los tributos y recargos aplicables. Se utiliza el Arancel de Aduanas del Perú, donde la subpartida nacional es un código de diez dígitos que identifica un producto específico. La clasificación se efectúa de acuerdo a la materia, su grado de elaboración, función, uso o destino.\n\n• Tributos y Recargos a la Importación: Todas las mercancías que se importen al Perú para su consumo están sujetas al pago de derechos arancelarios (ad-valorem), IGV e ISC. También pueden aplicarse Derechos Variables Adicionales, Antidumping y Compensatorios. La base imponible para la determinación de estos tributos se expresa en dólares y se cancela en moneda nacional al tipo de cambio venta vigente.",
                "confidence": 0.95
            },
            {
                "question_patterns": [
                    "para qué sirve el RUC en Perú",
                    "obtener RUC para importar/exportar",
                    "clave SOL SUNAT ¿qué es?",
                    "inscripción al RUC persona natural vs. jurídica",
                    "activar RUC y Clave SOL",
                    "importar sin RUC en Perú",
                    "quiénes necesitan RUC para trámites aduaneros?"
                ],
                "answer": "El Registro Único de Contribuyentes (RUC) y la Clave SOL son herramientas esenciales y obligatorias para la mayoría de las personas y empresas que desean participar en operaciones de comercio exterior en Perú. El RUC es un número de once dígitos que te identifica como contribuyente ante la SUNAT. La Clave SOL es un texto conformado por números y letras que te brinda acceso a los servicios y operaciones en línea de la SUNAT, permitiéndote realizar diversos trámites, consultas y pagos en Sunat Virtual. Generalmente se solicita y obtiene al momento de la inscripción del RUC.",
                "confidence": 0.95
            },
            {
                "question_patterns": [
                    "mercancías prohibidas Perú",
                    "mercancías restringidas Perú",
                    "qué productos no puedo importar a Perú",
                    "permisos para importar productos restringidos",
                    "VUCE para mercancías restringidas",
                    "lista de mercancías prohibidas SUNAT",
                    "documentos de control para importación",
                    "cómo saber si necesito permiso para importar"
                ],
                "answer": "Si estás planeando traer mercancías al país o enviarlas al exterior, es fundamental conocer si están clasificadas como prohibidas o restringidas. Las mercancías prohibidas son aquellas que, por mandato legal, se encuentran impedidas de ingresar o salir del país. Las mercancías restringidas, por otro lado, sí pueden, pero deben contar con documentos de control (permisos, autorizaciones, licencias o certificaciones) que amparen su ingreso o salida. Para consultar, puedes usar el portal de la SUNAT o la Plataforma de Tratamiento Arancelario por Subpartida Nacional e ingresar el código de 10 dígitos de tu mercancía. Para obtener los documentos de control para las mercancías restringidas, puedes gestionarlos de forma virtual a través de la Ventanilla Única de Comercio Exterior (VUCE).",
                "confidence": 0.95
            }
        ]

    def find_best_answer(self, user_question):
        best_match = None
        highest_score = 0
        clean_question = user_question.lower().strip()

        for qa in self.qa_pairs:
            for pattern in qa["question_patterns"]:
                similarity = SequenceMatcher(None, clean_question, pattern).ratio()
                if similarity > highest_score:
                    highest_score = similarity
                    best_match = qa

        if highest_score > 0.7 and best_match:
            return best_match["answer"]
        else:
            return None