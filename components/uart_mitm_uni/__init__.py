import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import uart
from esphome.const import CONF_ID

DEPENDENCIES = ['uart']

serial_ns = cg.esphome_ns.namespace('serial')

UARTMITMUNI = serial_ns.class_('UARTMITMUNI', cg.Component)

CONF_UART_IN = "uart_in"
CONF_UART_OUT = "uart_out"

CONFIG_SCHEMA = cv.COMPONENT_SCHEMA.extend({
    cv.GenerateID(): cv.declare_id(UARTMITMUNI),
    cv.Required(CONF_UART_IN): cv.use_id(uart.UARTComponent),
    cv.Required(CONF_UART_OUT): cv.use_id(uart.UARTComponent),
})


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)

    uart_in = await cg.get_variable(config[CONF_UART_IN])
    cg.add(var.set_uart_in(uart_in))
    uart_out = await cg.get_variable(config[CONF_UART_OUT])
    cg.add(var.set_uart_out(uart_out))
