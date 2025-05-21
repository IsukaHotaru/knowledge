# Abstract

## Background
1. While fine-tuned large language models (LLMs) excel in generating grammatically valid SQL in Text-to-SQL parsing, they often struggle to ensure semantic accuracy in queries, leading to user confusion and diminished system usability.

### Summary
1. LLM is good at SQL to text parsing, but it's not accurate enough in semantics, resulting in  less usability and satisfaction.

#### Template
- While ... excel in ..., they often struggle to ..., leading to ...

## Methods
1. To tackle this challenge, we introduce SQLFixAgent, a new consistency-enhanced multi-agent collaborative framework designed for detecting and repairing erroneous SQL. 
2. Our framework comprises a core agent, SQLRefiner, alongside two auxiliary agents: SQLReviewer and QueryCrafter.
3. The SQLReviewer agent employs the rubber duck debugging method to identify potential semantic mismatches between SQL and user query.
4. If the error is detected, the QueryCrafter agent generates multiple SQL as candidate repairs using a fine-tuned SQLTool.
5. Subsequently, leveraging similar repair retrieval and failure memory reflection, the SQLRefiner agent selects the most fitting SQL statement from the candidates as the final repair.

### Summary
1. We proposed a new model named SQLFixAgent, composed of a core agent SQLRefiner along with two auxiliary agents SQLReviewer and QueryCrafter. 
2. The data process is as follows: the SQLReviwer agent paraphrases SQL statements to identify semantic mismatches if there exists, then the QueryCrafter agent generates multiple SQL candidate statementes, and finally the SQLRefiner agent select the most fitting one through similar repair retrieval and failure memory reflection.

### Template
- To tackle this challenge, we introduce ..., a ... designed for ... .
- Our framework comprises ..., alongside ... .
- ... employs ... method to ...
- If ..., ... generates ... as ... using ....
- Subsequently, leveraging ..., ... selects ... from ... as ... .

## Results
1. We evaluated our proposed framework on five Text-to-SQL benchmarks.
2. The experimental results show that our method consistently enhances the performance of the baseline model, specifically achieving an execution accuracy improvement of over 3% on the Bird benchmark.
3. Our framework also has a higher token efficiency compared to other advanced methods, making it more competitive.

### Summary
1. The experiments show that our method consistently outperforms the baseline model, especially achieving an execution 3% accuracy improvement.
2. Our framework also has a higher process speed in tokenizating, making it better.

### Template
- The experimental results show that our method consistently enhances the performance of the baseline model, specifically achieving an execution accuracy improvemnet of over x% on ... benchmark.
- Our ... also has a higher ... compared to other advanced methods, making it more competitive.

# Introduction

## Background & Motivations
1. Traditional data querying methods require users to have expertise in Structured Query Language (SQL), posing a significant barrier for non-technical users.
2. Text-to-SQL parsing aims to overcome this obstacle by automatically converting natural language questions into SQL queries (Qin et al. 2022; Deng, Chen, and Zhang 2022).
3. Previous Text-to-SQL methods mainly rely on pretrained models to encode the input sequence (Wang et al. 2020; Hui et al. 2022), then decode the SQL query using abstract syntax trees (AST) (Guo et al. 2019; Wang et al. 2020; Cao et al. 2023).
4. However, recent advancements in decoder-based LLMs have transformed the field of NLP.
5. The researchers are actively exploring the potential of LLMs in Text-to-SQL parsing. These methods can be divided into two categories: Fine-tuning LLMs and Prompting LLMs.
6. The former fine-tunes the LLMs on Text-to-SQL downstream tasks, aiming to enhance their capabilities by high-quality data (Li et al. 2024a; Sun et al. 2024).
7. The latter prompts the proprietary LLMs with hundreds of billions parameters, such as GPT-4(OpenAI et al. 2024), to push the boundaries of Text-to-SQL by leveraging their superior In-Context-Learning capabilities (Gao et al. 2024; Wang et al. 2024a; Xie et al. 2024).
8. However, it is worth noting that due to the concerns of inference overheads and data privacy, Fine-tuning LLMs remains the preferred choice for most practical applications.
9. With the improvement of open source LLMS (Touvron et al. 2023; Li et al. 2023c), these methods achieved commendable performance on some simpler Text-to-SQL benchmarks (Yu et al. 2018, 2019), comparable to those state-of-the-art prompting-based methods.
10. Although the fine-tuned LLMs excel in generating syntactically valid SQL statements, they often struggle to produce semantically consistent ones in real-world scenarios (Sun et al. 2023) .
11. Given user query and the database schema, Figure 1 illustrates two types of errors in LLM-generated SQL: syntax errors and semantic errors.
12. Compared with syntax errors, semantic errors are more difficult to detect since they can be executed smoothly in the database.
13. These semantic errors lead to confusing execution results, significantly reducing the reliability of the Text-to-SQL system.

## Contributions-1
1. To enhance the capability of Text-to-SQL system in generating semantically accurate results, we introduce SQLFixAgent, a consistency-enhanced multi-agent collaborative framework designed to detect and correct errors in SQL generated by LLMs.
2. Our framework comprises a core *SQLRefiner* agent for repair decision, accompanied by two auxiliary agents, *SQLReviewer* and *QueryCrafter*, for latent error detection and candidate SQL generation.
3. Specifically, the SQLReviewer employs the Rubber Duck Debugging method to identify potential semantic discrepancies between SQL and user query, then initiate the repair request to other agents. 
4. Upon receiving the request, the QueryCrafter utilizes SQLTool to generate multiple SQL, then, the SQLRefiner selects the ones that best align with the query as the final repair from the candidates by retrieving similar repair examples and reflecting from failure memory.

## Experiments
1. In our experiments, we use the fine-tuned Codes (Li et al. 2024a) as the SQLTool used by agents for Text-to-SQL parsing and employ GPT-3.5-turbo as the backbone LLM for three agents.
2. We evaluate our framework on five Text-to-SQL benchmarks: Bird (Li et al. 2024b), Spider (Yu et al. 2018) and its three robustness variants (Gan, Chen, and Purver 2021; Gan et al. 2021; Deng et al. 2021).
3. The experimental results demonstrate that our SQLFixAgent can effectively reduce the syntatic and semantic errors generated by SQLTool.
4. On this basis, we conduct comprehensive ablation experiments on the framework.
5. We compare the fine-grained capabilities of the backbone LLMs and evaluate the agents' performance on sub-tasks, further revealing how the foundation LLMs serve as agents to assist the fine-tuned LLM in generating more semantic-accurate SQL queries.
6. Moreover, to achieve a practical Text-to-SQL solution, we compared the token efficiency of our approach with other advanced methods, demonstrating its competitive performance.

## Contributions-2
1. (1) We highlight the semantic inconsistency error between the LLM-generated SQL and the user's query in Text-to-SQL parsing.
2. To address this, we proposed SQLFixAgent, a consistency-enhanced collaborative framework designed to detect and repair the errors in LLM-generated SQL, including syntax and semantic errors.
3. (2) We conduct extensive evaluation and analysis on five Text-to-SQL benchmarks, demonstrating that our framework consistently enhances the performance of the baseline model, specifically achieving an execution accuracy improvement of over 3% on the Bird benchmark.
(4) Additionally, our approach achieves higher token efficiency compared to other advanced methods, enhancing its competitiveness.

## Related Work
Text-to-SQL with LLMs
#### Prompting LLMs
1. Recent advancements in large language models (LLMs) have resulted in groundbreaking capability (OpenAI et al. 2024; Team et al. 2024). 
2. To explore the potential of foundation LLMs in Text-to-SQL parsing, advanced prompting approaches tailored to the task have been proposed. 
3. DAIL-SQL (Gao et al. 2024) systematically examined prompt engineering for LLM-based Text-to-SQL methods, it employed dynamic few-shot examples by considering the similarity of both the user questions and the SQL queries.
4. Subsequent sutdies introduced frameworks like DIN-SQL (Pourreza and Rafiei 2023), C3-SQL (Dong et al. 2023), and StructGPT (Jiang et al. 2023), which aim to verify user queries, simplify databases representation, generate and integrate answers by utilizing techniques such as self-consistency (Wei et al. 2022a), chains of thought (Zhou et al. 2023).
5. However, they overly rely on the capability of proprietary LLms with hundreds of billions of parameters, raising concerns of data privacy and inference overheads.

#### Fine-tuning LLMs
1. Compared to prompting LLMs, fine-tuning LLMs is more widely adopted in enterprises. DAIL-SQL (Gao et al. 2024) has investigated fine-tuning open-source LLMs.
2. However, due to the smaller sizes, their performance remains lower than prompting larger LLMs such as GPT-4. Some research is dedicated to improving the capabilities of fine-tuned LLMs. CodeS (Li et al. 2024a) applied an incremental pre-training technique to train the Text-to-SQL LLMs on a meticulously constructed pre-training corpus, and achieves impressive results.
3. SQL-PaLM (Sun et al. 2024) focuses on larger-scale LLMs, investigating the potential for significant gains with increased model size due to the emergent capabilities of LLMs.
4. However, although the fine-tuned LLMs excel at generating syntactically valid SQL statements, they often struggle to produce semantically accurate queries, which is the challenge we need to address.

#### LLM-based Agents
1. Following the rise of large language models, LLM-based agents have become one of the mose prevalent AI systems (Wang et al. 2024b; Xi et al. 2023; Durante et al. 2024).
2. These agents learn to interact with the external world through action-observaton pairs articulated in natural language.
3. AutoGPT (AutoGPT-Team 2023) is an early open-source implementation of the AI agent, following a single-agent paradigm.
4. It enhances the AI model with a number of useful tools but lacks support for multi-agent collaboration.
5. In the programming domain, MetaGPT (Hong et al. 2023) innovatively simulates the operational structure of a traditional software company.
6. This framework drives the GPT agents to collaborate on user-defined programming tasks by assigning them to different roles: product manager, project manager, or engineer.
7. Similar work includes FixAgent (Lee et al. 2024), an automated and integrated debugging framework that achieves its goal through the collaboration of multiple agents.
8. In the Text-to-SQL field, MAC-SQL (Wang et al. 2024a) introduced a pioneering multi-agent framework, enabling multiple LLM-based agents to collaboratively tackle Text-to-SQL parsing tasks and effectively manage the complexity and diversity encountered in read-world query scenarios.
9. However, the application of LLM-based agents to detect and fix SQL errors generated by fine-tuned LLMs remains under-explored, which is our primary focus.

# Method

## Overview
1. We introduce SQLFixAgent, a consistency-enhanced multi-agent collaborative framework designed to detect and repair the syntax and semantic errors in SQL generated by SQLTools.
2. As illustrated in Figure 2, our framework comprises a core SQLRefiner agent for generating the final repaired SQL, accompanied by two auxiliary agents, the SQLReviewer and the QueryCrafter, for syntactic and semantic error detection and candidate repair generation.
3. Specifically, the SQLReviewer employs the Rubber Duck Debugging method to check whether the SQL aligns with the user's query intent.
4. If the error is detected, the SQLRefiner and QueryCrafter is tasked with making the SQL correction.
5. Specifically, the QueryCrafter utilizes SQLTool to generates multiple candidate SQL statements and the SQLRefiner selects the most appropriate one as the final repair by retrieving similar repair and reflecting from failure memory.

## SQLReviewer
1. LLM-based Text-to-SQL parsing typically encounters two types of errors: syntax errors and semantic errors.
2. The former can usually be detected and intercepted through the pre-execution check in database.
3. In contrast, the latter can be executed smoothly, producing confusing results for the user and reducing the reliability of system.
4. SQLReviewer is designed to detect the potential errors in SQL statements generated by LLMs.
5. We provide SQLReviewer with a real environment connected to the database to capture syntax errors in SQL.
6. Then, for those pass the syntax inspection, we further check whether their semantics align with the user's query based on the relevant database schema and evidence.
7. Based on the opinion: LLMs closely mimic developers when performing coding-related tasks, so they can benefit from general software engineering principles (Lee et al. 2024).
8. We adopt the principle of rubber duck debugging in the design of SQLReviewer, a method where a programmer explains his code line-by-line to an inanimate object (like a rubber duck) to help identify and understand errors, as shown in the Figure 3.
9. We assign SQLReviewer the role of a database administrator and require it to step-by-step verify whether each part of the SQL statement aligns with the user's query intent, thereby detecting potential semantic mismatch errors.
10. If no error is detected, the originial SQL will be returned as the final result.
11. Otherwise, the message will be passed to other agents for further processing.

## QueryCrafter
1. Although the fine-tuned LLMs excels at generating syntactically correct SQL statements, it remains challenging to produce ones that completely align with the user's query intent (Sun et al. 2023).
2. To mitigate this challenge, we designed QueryCrafter, which leverages SQLTool to generate multiple candidate SQL for SQLRefiner to select the most semantic-accurate one as the final repair.
3. Given a user query $Q$, QueryCrafter generates a list of variants $Q' = \{Q'_1, Q'_2, \ldots, Q'_n\}$ with similar length snd equivalent semantics.
4. Then, by using SQLTool, QueryCrafter generates multiple SQL statements $y = \{y_1, y_2, \ldots , y_m\}$ based on query variants Q', the database schema S and the evidence K.
5. The candidate SQL statements $y_{candidate} = \{y_1, y_2, \ldots, y_n \}$, which will be passed to SQLRefiner, are obtained by further pre-execution filtering of the SQL  statements $y$ in the database $D$.
6. Some researches showed that employing beam search decoding for LLMs to generate multiple candidate SQL can effectively improve the Text-to-SQL accuracy (Li et al. 2023a, 2024a).
7. However, the fine-tuned LLMs tend to overfit the training data, reducing the diversity of effective candidates.
8. In contrast, QueryCrafter generates multiple equivalent user queires, introducing perturbations at the input of SQLTool to broaden the spectrum of generated candidates.

## SQLRefiner
1. As the core of our SQLFixAgent framework, the primary function of SQLRefiner is to determine the final repair of SQL errors.
2. Since it is powered by a foundation LLM that is not specifically trained for Text-to-SQL tasks, it lacks proficiency in directly generating accurate SQL statements but excels in semantic analysis and comprehension.
3. Therefore, we regard SQLRefiner as essential for ensuring the framework produces semantically correct SQL.
4. Given the user query $Q$, the evidence $K$, and the database schema $S$, SQLRefiner retrieves similar repairs from the SQLTool error record as correction examples.
5. Then, it selects the SQL $y$ that best matches the user query from the candidate SQL $y_{candidate}$ provided by QueryCrafter as the final repair, along with explanation.
6. In some cases where QueryCrafter can not provide effective SQL candidates, SQLRefiner will attempt to correct the SQL statement on its own.
7. Despite some prompting tricks being used to guide the LLMs toward expected outcomes, achieving an error-free repair in a single attempt remains difficult due to the hallucination of LLM (Huang et al. 2023). 
8. To mitigate this challenge, we introduced Reflexion (Shinn et al. 2023) mechanism in SQL repair.
9. As shown in Figure 4.
10. Upon selection or generation of a SQL statement, following MAC-SQL (Wang et al. 2024a), the SQLRefiner first assess its syntactic correctness, execution feasibility, and the retrieval of non-empty results from the database.
11. If the check passes, the SQL statement will be taken as the final repair; otherwise, it will be written into the failure memeory along with the execution error feedback from database.
12. In the next attempt, SQLRefiner reflects on the failure memory and repeats the repair process until the generated result passes the execution check or the maximum number of correction is reached.
13. The essence of the SQLFixAgent framework lies in the collaboration between a foundational LLM and a specialized LLM trained on Tex-to-SQL task.
14. We believe their capabilities are complementary: While the foundational LLM possesses strong ICL abilities, it is not adept at generating effective SQL statements directly.
15. On the other hand, the Text-to-SQL LLM excels at generating syntactically valid SQL statements, but often struggles to produce ones with semantic consistency.
16. In the SQLFixAgent framework, the correctness of SQL syntax is primarily ensured by SQLTool, while the consistency of SQL semantics is guaranteed through the collaboration of QueryCrafter and SQLRefiner.

# Experiments

## Datasets
1. We evluated our framework on two primary Text-to-SQL benchmarks: Spider (Yu et al. 2018) and Bird (Li et al. 2024b).
2. Moreover, we assessed the robustness on three variants of Spider: Spider-DK (Gan, Chen and Purver 2021), Spider-Syn (Gan et al. 2021), and Spider-Realistic (Deng et al. 2021).
3. For the training sets of Spider and Bird, we used them to simulate runtime error record.

### Spider
1. Spider is widely used to evaluate Text-to-SQL parsers across various databases, requiring models to demonstrate their adaptability to unfamiliar database structures.
2. It offers a training set comprising 8,659 samples, a development set with 1,034 samples, and a test with 2,147 samples, encompassing 200 distinct databases and 138 domains.

### BIRD
1. BIRD released by Alibaba DAMO Academy, is a new benchmark for large-scale database grounded Text-to-SQL evaluation.
2. It contains 95 large-scale databases and high-quality Text-SQL pairs, with a data storage volume of up to 33.4GB spanning 37 professional domains.
3. Compared to Spider, it focuses on integrating external knowledge reasoning to bridge natural language questions and database content, and addresses new challenges related to SQL efficiency when handling large databases.

### Spider-DK, Spider-Syn, Spider-Realistic
1. Spider-DK, Spider-Syn, Spider-Realistic are variants derived from the original Spider dataset, introducing robustness challenges through domain knowledge introduction, synonym sustitution, and explicit mention removal, respecitively.
2. They are specifically crafted to resemble queries that might be posed by users in read-world scenarios.

## Evaluation Metrics
1. We adopt execution accuracy, exact match accuracy, and valid efficency score to evaluate the performance of our framework. 
2. *Execution accuracy (EX)* is defined as the proportion of questions in the evaluation set where the execution result of both the predicted and ground-truth queries are identical.
3. *Exact match accuracy (EM)*, introduced by Test-Suites (Zhong, Yu, and Klein 2020), evaluates each clause as a set and compares the predicted clauses with their corresponding ones in the **reference query**.
4. A predicted SQL query is considered correct only if all of its components match the ground truth. 
5. *Valid efficency score (VES)*, introduced by Bird (Li et al. 2024b), is designed to measure the efficiency of valid SQL. It considers both the accuracy and efficiency for the model-generated query.

## Implementation Details
1. In evaluation, we utilized fine-tuned version of CodeS (Li et al. 2024a) with 3b and 7b parameters as the SQLTool within the framework, and all agents were powered by GPT-3.5-turbo.
2. For SQLTool inference, a **beam search** produces 4 SQL candidates, we select the first executable one for further checking by SQLFixAgent.
3. If the error is detected, SQLFixAgent attempts to repair it up to 3 times.
4. These hyperparameters are tuned on validation set.
5. All experiments were conducted on a server equipped with 1 x AMD EPYC 7352 CPU and 8 x NVIDIA RTX 3090 GPU.
6. To facilitate the related research, all codes will be released via Github.

## Main Results

### Results on BIRD
1. Table 1 presents the performance of the SQLFixAgent framework compared to other competitive methods on the current most challenging Text-to-SQL benchmark, BIRD.
2. We observe that CodeS-7B + SQLFixAgent achieves better performance than standalone CodeS-7B, indicating that SQLFixAgent effictively reduces semantic and syntactic errors in the SQL generated by the LLMs.
3. Surprisingly, it outpuerforms DAIL0SQL by 5.41% EX with backbone models (CodeS-7B and GPT-3.5 Turbo) that their parameters significantly fewer than GPT-4, higlighting the value of SQL repair study.
4. Specifically, CodeS-7B equipped with SQLFixAgent demonstrated a 3.00% increase in EX and a 4.35% increase in VES, while CodeS-3B equipped with SQLFixAgent improved EX by 3.65% and VES by 5.65%, showing even greater improvement.
5. This result is attributed to the weaker capability of CodeS-3b, which leads to more correctable errors in the generated SQL.

### Results on Spider and its Variants
1. As shown in Table 2, SQLFixAgent enhanceds the EX performance of the CodeS-3B and CodeS-7B baseline by 1.4% and 0.8% on Spider's dev set.
2. Since SQLFixAgent is powered by GPT-3.5 Turbo without fine-tuning, it does not contribute to improving exact match accuracy.
3. On the other hand, CodeS-7B with SQLFixAgent shows a 0.6% EX improvement on test set.
4. This represents the performance limit of GPT-3.5 Turbo on Spider.
5. Across three robustness variants of Spider, as shown in Table 3, our framework achieved CodeS-7B EX improvement of 0.8%, 0.4%, and 2.2% on Spider-Syn, Spider-Realistic, and Spider-DK, respectively, reaching the state-of-the-art performance.
6. Particularly, the results from Spider-DK demonstrate that it significantly enhances the domain knowledge reasoning capability of fine-tuned LLMs.

## Ablation Study

### Analysis of Backbone Model Capabilities
1. Figure 5 illustrates the performance of the backbone models of SQLFixAgent across different sub-capability dimensions on Bird-dev.
2. The results indicate that fine-tuned CodeS-3B outperforms GPT-3.5 Turbo in all areas, particularly in ranking, numerical computing (math), and value illustration, with accuracy of GPT-3.5 Turbo in math and ranking below 30%.
3. It suggests that foundation LLMs struggle with deep data science tasks, which often require mathematical computations and rankings within the context of vauge user queires.
4. However, all models perform well in domain KG, synonym, and match-based areas, benefiting from language and reasoning abilities acquired during pre-training.
5. Despite GPT-3.5 Turbo's inferior performance compared to fine-tuned CodeS-3B across all fine-grained categories, we employ it as agents for error detection and correction on LLM-generated SQL, further improving the query accuracy of the system.

### Analysis of Performance on Sub-tasks
1. Our framework includes two main subtasks in Text-to-SQL parsing: SQL error detection and correction, which are respectively handled by the SQLReviewer agent and the SQLRefiner agent.
2. We employ F1 score to evaluate the performance of SQLReviewer in SQL error detection, and then calculate the repair success rate of SQLRefiner after the errors have been detected.
3. As shown in Table 4, our framework can effectively detect erroeous SQL statements, including both semantic and syntactic errors.
4. Due to the performance limitations of the backbone model, SQLFixAgent achieves repair success rates of 17.49% and 15.64% for errors generated by CodeS-3B and CodeS-7B, respectively.
5. This presents a challenging task, and we plan to delve deeper into it in future work.