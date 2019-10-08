import random
import sys
from person import Person
from logger import Logger
from virus import Virus
random.seed(42)


class Simulation(object):
    """Main class that will run the herd immunity simulation program.
    Expects initialization parameters passed as command line arguments when
    file is run.

    Simulates the spread of a virus through a given population.  The percentage
    of the
    population that are vaccinated, the size of the population, and the amount
    of initially
    infected people in a population are all variables that can be set when the
    program is run.
    """

    def __init__(self, pop_size, vacc_percentage, virus, initial_infected=1):
        """
        Logger object logger records all events during the simulation.
        Population represents all Persons in the population.
        The next_person_id is the next available id for all created Persons,
        and should have a unique _id value.
        The vaccination percentage represents the total percentage of
        population vaccinated at the start of the simulation.
        You will need to keep track of the number of people currently infected
        with the disease.
        The total infected people is the running total that have been infected
        since the
        simulation began, including the currently infected people who died.
        You will also need to keep track of the number of people that have die
        as a result
        of the infection.

        All arguments will be passed as command-line arguments when the file is
        run.
        HINT: Look in the if __name__ == "__main__" function at the bottom.
        """
        # TODO: Create a Logger object and bind it to self.logger.
        # Remember to call the appropriate logger method in the corresponding
        # parts of the simulation.
        # TODO: Call self._create_population() and pass in the correct
        # parameters.
        # Store the array that this method will return in the self.population
        # attribute.
        # TODO: Store each newly infected person's ID in newly_infected
        # attribute.
        # At the end of each time step, call self._infect_newly_infected()
        # and then reset .newly_infected back to an empty list.
        self.pop_size = pop_size  # Int
        self.next_person_id = 0  # Int
        self.virus = virus  # Virus object
        self.initial_infected = initial_infected  # Int
        self.total_infected = 0  # Int
        self.current_infected = 0  # Int
        self.vacc_percentage = vacc_percentage  # float between 0 and 1
        self.population = self._create_population(self.initial_infected)
        self.total_dead = 0  # Int
        self.file_name = "{}_simulation_pop_{}_vp_{}_infected_{}.txt".format(
            virus_name, pop_size, vacc_percentage, initial_infected)
        self.logger = Logger(self.file_name)
        self.newly_infected = []

    def _create_population(self, initial_infected):
        """
        This method will create the initial population.
            Args:
                initial_infected (int): The number of infected people that the
                simulation
                will begin with.

            Returns:
                list: A list of Person objects.

        """
        person_list = []

        for number in range(self.pop_size):
            person_list.append(Person(number, False))

        for number in range(self.initial_infected):
            person_list[number].infection = self.virus

        vaccinated_people = self.vacc_percentage * self.pop_size  
        for number in range(vaccinated_people):
            person_list[number+self.initial_infected].is_vaccinated = True

        return person_list
        # TODO: Finish this method!  This method should be called when the
        # simulation
        # begins, to create the population that will be used. This method
        # should return
        # an array filled with Person objects that matches the specifications
        # of the
        # simulation (correct number of people in the population, correct
        # percentage of
        # people vaccinated, correct number of initially infected people).

        # Use the attributes created in the init method to create a population
        # that has
        # the correct intial vaccination percentage and initial infected.
       

    def _simulation_should_continue(self):
        """
        The simulation should only end if the entire population is dead
        or everyone is vaccinated.

            Returns:
                bool: True for simulation should continue, False if it should
                end.

        """
        for person in self.population:
            if person.infection == self.virus and person.is_alive == False:
                return True
        return False    
        
        # TODO: Complete this helper method.  Returns a Boolean.
        

    def run(self):
        """
        This method should run the simulation until all requirements for ending
        the simulation are met.
        """
        # TODO: Finish this method.  To simplify the logic here, use the helper
        # method
        # _simulation_should_continue() to tell us whether or not we should
        # continue
        # the simulation and run at least 1 more time_step.

        # TODO: Keep track of the number of time steps that have passed.
        # HINT: You may want to call the logger's log_time_step() method at the
        # end of each time step.
        # TODO: Set this variable using a helper
        time_step_counter = 0
        should_continue = None

        while self._simulation_should_continue():
            self.time_step()
            self.logger.log_time_step(time_step_counter)
            time_step_counter += 1
            # TODO: for every iteration of this loop, call self.time_step() to
            # compute another
            # round of this simulation.
        print('The simulation has ended after',
              '{time_step_counter} turns.'.format(time_step_counter))
        

    def time_step(self): #Chudier
        """
        This method should contain all the logic for computing one time step
        in the simulation.

        This includes:
            1. 100 total interactions with a randon person for each infected
            person in the population
            2. If the person is dead, grab another random person from the
            population.
                Since we don't interact with dead people, this does not count
                as an interaction.
            3. Otherwise call simulation.interaction(person, random_person) and
                increment interaction counter by 1.
        """
        sick_list = []
        for person in self.population:
            if person.infection == self.virus & person.is_alive == True:
                sick_list.append(person)

        for person in sick_list:
            counter = 0
            while counter < 100:
                random = random.choice(self.population)

                while random.is_alive == False:
                    random = random.choice(self.population)

                self.interaction(person,random)
                counter += 1                

        for person in sick_list:
            person.did_survive_infection()

        self._infect_newly_infected()
        # TODO: Finish this method.
        pass

    def interaction(self, person, random_person): #Chudier
        """
        This method should be called any time two living people are selected
        for an
        interaction. It assumes that only living people are passed in as
        parameters.

        Args:
            person1 (person): The initial infected person
            random_person (person): The person that person1 interacts with.

        """
        # Assert statements are included to make sure that only living people
        # are passed
        # in as params
        assert person.is_alive is True
        assert random_person.is_alive is True

        # TODO: Finish this method.
        #  The possible cases you'll need to cover are listed below:
        # random_person is vaccinated:
        #     nothing happens to random person.
        # random_person is already infected:
        #     nothing happens to random person.
        # random_person is healthy, but unvaccinated:
        #     generate a random number between 0 and 1.  If that number is
        # smaller
        #     than repro_rate, random_person's ID should be appended to
        #     Simulation object's newly_infected array, so that their .infected
        #     attribute can be changed to True at the end of the time step.
        # TODO: Call slogger method during this method.

        if random_person.is_vaccinated:
            pass
        elif random_person.infection == self.virus:
            pass
        else:
            if random.random() < self.virus.repro_rate:
                self.newly_infected.append(random_person)
        

    def _infect_newly_infected(self): #Chudier
        """
        This method should iterate through the list of ._id stored in
        self.newly_infected
        and update each Person object with the disease.
        """
        for person in self.newly_infected:
            person.infection = self.virus

        self.newly_infected.clear()
        # TODO: Call this method at the end of every time step and infect each
        # Person.
        # TODO: Once you have iterated through the entire list of
        # self.newly_infected, remember
        # to reset self.newly_infected back to an empty list.
        pass


if __name__ == "__main__":
    params = sys.argv[1:]
    virus_name = str(params[0])
    repro_num = float(params[1])
    mortality_rate = float(params[2])

    pop_size = int(params[3])
    vacc_percentage = float(params[4])

    if len(params) == 6:
        initial_infected = int(params[5])
    else:
        initial_infected = 1

    virus = Virus(virus_name, repro_num, mortality_rate)
    sim = Simulation(pop_size, vacc_percentage, initial_infected, virus)

    sim.run()
