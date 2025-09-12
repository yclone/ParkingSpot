from flask import Blueprint, request
import logging

log_bp = Blueprint('log', __name__)

@log_bp.route('/log', methods=['POST'])
def log_message():
    try:
        data = request.get_json()
        message = data.get('message', '')
        with open('frontend_logs.txt', 'a', encoding='utf-8') as log_file:
            log_file.write(f"{message}\n")
        return {'message': 'Log registrado com sucesso!'}, 200
    except Exception as e:
        logging.error(f"Erro ao registrar log: {str(e)}")
        return {'message': 'Erro ao registrar log'}, 500