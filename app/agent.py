import os
from openai import OpenAI
from dotenv import load_dotenv
import re
from loguru import logger
from actions import (
    search_flights, find_hotels, get_attractions,
    recommend_restaurants, get_weather, convert_currency, translate_text
)

load_dotenv()

logger.add("travel_agent.log", rotation="500 MB")


class TravelAgent:
    def __init__(self, system_prompt, initial_budget=1000):
        self.system_prompt = system_prompt
        self.budget = initial_budget
        self.messages = [
            {'role': 'system', 'content': system_prompt},
            {'role': 'system', 'content': f'The current budget is ${self.budget}.'},
            {'role': 'system',
             'content': 'You are a React agent. Follow this loop: Thought, Action, Observation. Use "Thought:" to explain your reasoning, "Action:" to specify an action, and wait for an "Observation:". When you have a complete travel plan, state "Final Answer:" followed by the detailed plan.'}
        ]
        self.thoughts = []
        self.actions = {
            'search_flights': search_flights,
            'find_hotels': find_hotels,
            'get_attractions': get_attractions,
            'recommend_restaurants': recommend_restaurants,
            'get_weather': get_weather,
            'convert_currency': convert_currency,
            'translate_text': translate_text
        }
        self.client = OpenAI(
            base_url="https://api.groq.com/openai/v1",
            api_key=os.environ.get("GROQ_API_KEY")
        )
        self.model = 'mixtral-8x7b-32768'
        logger.info("TravelAgent initialized")

    def plan_trip(self, user_input, max_turns=15):
        logger.info(f"Starting trip planning for user input: {user_input}")
        self.messages.append({"role": "user", "content": user_input})

        for turn in range(max_turns):
            logger.info(f"Turn {turn + 1}/{max_turns}")
            response = self._get_llm_response()
            self.messages.append({"role": "assistant", "content": response})
            logger.info(f"LLM Response: {response}")

            thought, action, final_answer = self._parse_response(response)

            if thought:
                self.thoughts.append(thought)
                logger.info(f"Thought: {thought}")

            if final_answer:
                logger.info(f"Final Answer: {final_answer}")
                return final_answer

            if action:
                result = self._execute_action(action)
                observation = f"Observation: {result}"
                self.messages.append({"role": "system", "content": observation})
                logger.info(f"Action: {action}")
                logger.info(observation)
            else:
                logger.warning("No action taken in this turn")

        logger.warning("Max turns reached without final answer")
        return self._generate_incomplete_plan()

    def _get_llm_response(self):
        try:
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=self.messages,
                temperature=0.7
            )
            return completion.choices[0].message.content
        except Exception as e:
            logger.error(f"Error getting LLM response: {e}")
            return "I apologize, but I encountered an error. Please try again."

    def _parse_response(self, response):
        thought_match = re.search(r'Thought: (.+?)(?=\n|$)', response, re.DOTALL)
        action_match = re.search(r'Action: (.+?)(?=\n|$)', response, re.DOTALL)
        final_answer_match = re.search(r'Final Answer: (.+)', response, re.DOTALL)

        thought = thought_match.group(1).strip() if thought_match else None
        action = action_match.group(1).strip() if action_match else None
        final_answer = final_answer_match.group(1).strip() if final_answer_match else None

        return thought, action, final_answer

    def _execute_action(self, action_string):
        action_match = re.match(r'(\w+): (.+)', action_string)
        if action_match:
            action, params_string = action_match.groups()
            if action in self.actions:
                params = [param.strip() for param in params_string.split(',')]
                try:
                    return self.actions[action](*params)
                except Exception as e:
                    logger.error(f"Error executing action {action}: {e}")
                    return f"Error executing {action}: {str(e)}"
        logger.warning(f"Invalid action: {action_string}")
        return "Action could not be executed."

    def _generate_incomplete_plan(self):
        incomplete_plan = "I apologize, but I couldn't complete the full travel plan within the allowed steps. Here's what I have so far:\n\n"
        for thought in self.thoughts:
            incomplete_plan += f"- {thought}\n"
        incomplete_plan += "\nPlease provide more specific requirements or ask for details on any part of the plan."
        return incomplete_plan

    def get_thoughts(self):
        return self.thoughts