package me.thomassuebwicha.repository;

import java.util.List;

import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

import me.thomassuebwicha.entity.ThemeParkRide;

@Repository
public interface ThemeParkRideRepository extends CrudRepository<ThemeParkRide, Long>{
	List<ThemeParkRide> findByName(String name);
}
